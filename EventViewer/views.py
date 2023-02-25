from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from EventViewer.forms import SignUpForm, EventForm
from EventViewer.models import Event, Category, Comment


# Create your views here.


def home_page(request):
    upcoming_events= Event.objects.filter(id=1)
    context= {'upcoming_events':upcoming_events}
    return render(request, 'home.html', context)


def event_page(request):
    categories = Category.objects.all()
    events = Event.objects.all()
    context = {'events': events,'categories':categories}
    return render(request, 'events.html', context)



def filter_events(request):
    categories = Category.objects.all()
    selected_category = request.POST.get('category', '')
    min_price = request.POST.get('min_price')
    max_price = request.POST.get('max_price')
    upcoming_events = request.POST.get('upcoming_events')
    past_events = request.POST.get('past_events')

    if min_price == '':
        min_price =0
    if max_price == '':
        max_price =10000

    if selected_category:
        events = Event.objects.filter(Q(price__gt=min_price)& Q(price__lt=max_price) & Q(category=selected_category))
    else:
        events = Event.objects.filter(Q(price__gt=min_price) & Q(price__lt=max_price))

    if upcoming_events and  past_events:
        events = events.all()
    elif upcoming_events:
        events = events.filter(start_at__gt=datetime.now())
    elif past_events:
        events = events.filter(start_at__lt=datetime.now())

    context = {'categories': categories, 'events': events}
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





def search_events(request):
    if request.method == 'POST':
        search = request.POST.get('query')
        search = search.strip()
        if len(search) > 0:
            events = Event.objects.filter(name__contains=search)
            if len(events) == 0:
                messages.info(request, "Cant find your event.")
            context = {'search': search, 'events': events}
            return render(request, 'events.html', context)
        else:
            messages.info(request, "Cant find your event.")
    return render(request, 'home.html')


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


