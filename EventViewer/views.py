from django.shortcuts import render

# Create your views here.



def home_page(request):

    return render(request, 'home.html')


def event_page(request):

    return render(request, 'events.html')