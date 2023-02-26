from datetime import datetime
from django.contrib.sites import requests
from django.contrib import messages
from django.shortcuts import render
from rest_framework import generics
from API.serializers import EventSerializer
from EventViewer.models import Event, Category
import requests

# Create your views here.


def get_events(request):
    if request.method == 'POST':
        try:
            page = request.POST.get('page')
            url = f'https://app.ticketmaster.com/discovery/v2/events?apikey=jztfUNwQzA2WdVkQCAt5fFDHOSqgWlfq&locale=*&page={page}'
            events = requests.get(url).json()['_embedded']['events']
            for e in events:
                try:
                    category_name = e['classifications'][0]['segment']['name']
                    category, created = Category.objects.get_or_create(name=category_name)

                    if 'pleaseNote' in e:
                        description = e['pleaseNote']
                    elif 'boxOfficeInfo' in e:
                        description = e['boxOfficeInfo']['phoneNumberDetail']
                    elif 'generalInfo' in e:
                        description = e['generalInfo']['generalRule']
                    else:
                        description = e['name']

                    if 'priceRanges' in e:
                        price = e['priceRanges'][0]['min']
                    else:
                        price = 0

                    event_data = {
                        'name': e['name'],
                        'category': category,
                        'city': e['_embedded']['venues'][0]['city']['name'],
                        'price': price,
                        'start_at': e['dates']['start']['dateTime'],
                        'link': e['url'],
                        'picture': e['images'][0]['url'],
                        'description': description,
                        'user_creator': request.user,
                    }

                    try:
                        Event.objects.get(name=event_data['name'], start_at=event_data['start_at'])
                    except Event.DoesNotExist:
                        Event.objects.create(**event_data)
                        messages.success(request, f"Event {event_data['name']} was added to database.")
                except Exception as exc:
                    raise exc
                finally:
                    continue
        except:
            messages.error(request, "Page is out of range")
    return render(request, 'get_events_API.html')


class EventListView(generics.ListAPIView):
    queryset = Event.objects.filter(start_at__gt=datetime.now())
    serializer_class = EventSerializer


class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.filter(start_at__gt=datetime.now())
    serializer_class = EventSerializer