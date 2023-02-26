from django.contrib.sites import requests
from django.shortcuts import render

from EventViewer.models import Event, Category
import requests

# Create your views here.


def get_events(request):
    url = 'https://app.ticketmaster.com/discovery/v2/events?apikey=jztfUNwQzA2WdVkQCAt5fFDHOSqgWlfq&locale=*&page=3'
    events = requests.get(url).json()['_embedded']['events']
    if request.method == 'POST':

        for e in events:
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
            event = Event.objects.create(**event_data)
    return render(request, 'get_events_API.html')
