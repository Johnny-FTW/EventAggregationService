from django.urls import path

from API import views


app_name = 'api'

urlpatterns = [
    path('get_events/', views.get_events, name ='get_events'),
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('events/<pk>/',views.EventDetailView.as_view(), name='event_detail'),

    ]