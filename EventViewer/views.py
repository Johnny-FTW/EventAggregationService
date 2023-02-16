from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from EventViewer.forms import SignUpForm, EventForm

from django.contrib.auth.views import LoginView

from EventViewer.models import Event


# Create your views here.


def home_page(request):
    return render(request, 'home.html')


def event_page(request):
    events = Event.objects.all()
    context = {'events': events}
    # if request_method ==
    return render(request, 'events.html', context)


@login_required
def event_detail_page(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event': event}
    return render(request, 'event_detail.html', context)


def search_events(request):
    if request.method == 'POST':
        search = request.POST.get('query')
        search = search.strip()
        if len(search) > 0:
            events = Event.objects.filter(name__contains=search)
            error_message = ''
            if len(events) == 0:
                error_message = "Cant find your event."
            context = {'search': search, 'events': events, 'error_message': error_message}
            return render(request, 'events.html', context)
        else:
            context = {'search': search, 'error_message': "Cant find your event."}
            return render(request, 'events.html', context)

    return render(request, 'home.html')


class EventCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'new_event.html'
    form_class = EventForm
    success_url = reverse_lazy('event_page')
    permission_required = 'viewer.add_event'


class EventUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'new_event.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('event_page')
    permission_required = 'viewer.edit_event'

# class EventDeleteView(PermissionRequiredMixin, DeleteView):
#     template_name = 'movie_confirm_delete.html'
#     model = Movie
#     success_url = reverse_lazy('home')
#     permission_required = 'viewer.delete_movie'




class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home_page')
    template_name = 'signup.html'
