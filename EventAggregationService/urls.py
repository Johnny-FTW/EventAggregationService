"""EventAggregationService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy

from EventViewer.views import home_page, event_page, SignUpView, event_detail_page, search_events, EventCreateView, \
    EventUpdateView, EventDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('events/', event_page, name='event_page'),
    path('event_detail/<pk>/', event_detail_page, name='event_detail_page'),
    path('search_events/', search_events, name='search_events'),

    #add, edit , delete event
    path('new_event/', EventCreateView.as_view(), name='new_event'),
    path('event/update/<pk>/', EventUpdateView.as_view(), name='update_event'),
    path('event_detail/<pk>/', EventDeleteView.as_view(), name='delete_event'),


    #users
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),

]
