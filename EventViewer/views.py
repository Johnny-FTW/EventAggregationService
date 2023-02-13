from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from EventViewer.forms import SignUpForm

from django.contrib.auth.views import LoginView

# Create your views here.



def home_page(request):

    return render(request, 'home.html')


def event_page(request):

    return render(request, 'events.html')


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home_page')
    template_name = 'signup.html'

