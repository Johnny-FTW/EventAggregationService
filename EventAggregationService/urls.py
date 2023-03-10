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

from EventViewer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('events/', event_page, name='event_page'),
    path('event_detail/<pk>/', event_detail_page, name='event_detail_page'),
    path('search_events/', search_events, name='search_events'),
    path('filter_events/', filter_events, name='filter_events'),

    #attending
    path('attend/', attend_event, name='attend_event'),

    #add, edit , delete event
    path('new_event/', EventCreateView.as_view(), name='new_event'),
    path('event/update/<pk>/', EventUpdateView.as_view(), name='update_event'),
    path('delete_event/<pk>/', EventDeleteView.as_view(), name='delete_event'),

    #comments
    path('add_comment/<pk>/', add_comment, name='add_comment'),
    path('edit_comment/<pk>', edit_comment, name='edit_comment'),
    path('delete_comment/<pk>/', delete_comment, name='delete_comment'),

    #users
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),

    #API
    path('api/', include('API.urls', namespace='api')),

]
