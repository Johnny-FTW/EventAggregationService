from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from EventViewer.forms import SignUpForm

from django.contrib.auth.views import LoginView

from EventViewer.models import Event


# Create your views here.



def home_page(request):

    return render(request, 'home.html')


def event_page(request):
    events = Event.objects.all()
    context = {'events':events}
    #if request_method ==
    return render(request, 'events.html',context)

def event_detail_page(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event':event}
    return render(request, 'event_detail.html', context)






class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home_page')
    template_name = 'signup.html'

