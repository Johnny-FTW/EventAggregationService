from django.urls import path

from API import views
from API.views import EventDetailApiView, EventListApiView, detail_api_view

app_name = 'api'

urlpatterns = [
    path('get_events/', views.get_events, name ='get_events'),

    path('events/', views.EventListView.as_view(), name='event_list'),
    path('events/<pk>/',views.EventDetailView.as_view(), name='event_detail'),
    path('', EventListApiView.as_view(), name = 'list_api_view'),
    path('<int:event_id>/', EventDetailApiView.as_view()),
    path('detail_api_view', detail_api_view, name='detail_api_view')
    ]