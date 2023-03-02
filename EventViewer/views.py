from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from EventViewer.forms import SignUpForm, EventForm
from EventViewer.models import Event, Category, Comment


# Create your views here.


def home_page(request):
    events= Event.objects.filter(start_at__gte= datetime.now())[:3]
    event_tips = Event.objects.filter(start_at__gte=datetime.now()).annotate(num_attendees=Count('user_attend')).order_by('-num_attendees')[:4]
    context= {'events':events, 'event_tips': event_tips}
    return render(request, 'home.html', context)


def paginate_queryset(request, queryset, page_size):
    paginator = Paginator(queryset, page_size)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def event_page(request):
    categories = Category.objects.all()
    events = Event.objects.filter(start_at__gte=datetime.now())
    page_obj = paginate_queryset(request, events, 20)

    context = {'page_obj': page_obj, 'categories': categories}
    return render(request, 'events.html', context)


def search_events(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        search = request.POST.get('query')
        search = search.strip()
        request.session['search'] = search
    else:
        search = request.session['search']
    if len(search) > 0:
        events = Event.objects.filter(name__contains=search)
        page_obj = paginate_queryset(request, events, 20)
        if len(events) == 0:
            messages.info(request, "Can't find your event.")
        context = {'search': search, 'page_obj': page_obj, 'categories': categories}
        return render(request, 'events.html', context)
    else:
        messages.info(request, "Can't find your event.")
    return render(request, 'events.html', {'categories': categories})


def filter_events(request):
    selected_category = request.session.get('selected_category', '')
    min_price = request.session.get('min_price', '')
    max_price = request.session.get('max_price', '')
    upcoming_events = request.session.get('upcoming_events', '')
    past_events = request.session.get('past_events', '')

    categories = Category.objects.all()

    if request.method == 'POST':
        selected_category = request.POST.get('category', '')
        min_price = request.POST.get('min_price', '')
        max_price = request.POST.get('max_price', '')
        upcoming_events = request.POST.get('upcoming_events', '')
        past_events = request.POST.get('past_events', '')

        request.session['selected_category'] = selected_category
        request.session['min_price'] = min_price
        request.session['max_price'] = max_price
        request.session['upcoming_events'] = upcoming_events
        request.session['past_events'] = past_events

    events = Event.objects.all()
    if selected_category:
        events = events.filter(category=selected_category)
    if min_price:
        events = events.filter(price__gte=min_price)
    if max_price:
        events = events.filter(price__lte=max_price)
    if upcoming_events and past_events:
        events = events

    elif upcoming_events:
        events = events.filter(start_at__gt=datetime.now())
    elif past_events:
        events = events.filter(start_at__lt=datetime.now())

    if not selected_category:
        selected_category = 0

    page_obj = paginate_queryset(request, events, 20)
    if not page_obj:
        messages.info(request, "Can't find your event.")
    context = {
        'categories': categories,
        'page_obj': page_obj,
        'selected_category': int(selected_category),
        'min_price': min_price,
        'max_price': max_price,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    }
    return render(request, 'events.html', context)





@login_required
def event_detail_page(request, pk):
    event = Event.objects.get(id=pk)
    comments = Comment.objects.filter(event=event).all()
    context = {'event': event, 'comments':comments}
    return render(request, 'event_detail.html', context)


@login_required
def attend_event(request):
    if request.method == 'POST':
        pk = request.POST.get('event_id')
        event = Event.objects.get(id=pk)
        if not request.user in event.user_attend.all():
            event.user_attend.add(request.user)
            messages.success(request, "You are attending this event. Have a fun!")
        else:
            event.user_attend.remove(request.user)
            messages.info(request, "You are not attending this event.")
    return redirect(f'/event_detail/{pk}/')


@login_required
def add_comment(request, pk):
    if request.method == 'POST':
        pk = request.POST.get('event_id')
        comment = request.POST.get('comment').strip()
        if len(comment) > 0:
            Comment.objects.create(
                event = Event.objects.get(id=pk),
                user = request.user,
                comment = comment
            )
            messages.success(request, "Your comment was posted.")
        else:
            messages.error(request, "Cant post your comment.")
    return redirect(f'/event_detail/{pk}/')


@login_required
def edit_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.user == comment.user:
        if request.method == 'POST':
            comment_text = request.POST.get('comment').strip()
            comment.comment = comment_text
            comment.save()
            messages.info(request, "Your comment was edited.")
            return redirect(f'/event_detail/{comment.event.id}/')
        context = {'comment':comment}
        return render(request, 'event_detail.html', context)
    return redirect(f'/event_detail/{comment.event.id}/')


@login_required
def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.user == comment.user:
        if request.method == 'POST':
            comment.delete()
            messages.info(request, "Your comment was deleted.")
            return redirect(f"/event_detail/{comment.event.id}/")

        # else
        context = {'comment': comment}
        return render(request, 'comment_confirm_delete.html', context)
    return redirect(f"/event_detail/{comment.event.id}/")


class EventCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'new_event.html'
    form_class = EventForm
    success_url = reverse_lazy('event_page')
    permission_required = 'viewer.add_event'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user_creator = self.request.user
        obj.save()
        return super().form_valid(form)


class EventUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'new_event.html'
    model = Event
    form_class = EventForm
    permission_required = 'viewer.edit_event'

    def get_success_url(self):
        return reverse_lazy('event_detail_page', kwargs={'pk': self.object.pk})


class EventDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'event_detail.html'
    model = Event
    success_url = reverse_lazy('event_page')
    permission_required = 'viewer.delete_event'


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home_page')
    template_name = 'signup.html'


