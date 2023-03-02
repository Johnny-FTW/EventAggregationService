from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from API.serializers import EventSerializer
from EventViewer.models import Event, Category
import requests

# Create your views here.

@login_required
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


class EventListApiView(APIView):

    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        queryset = Event.objects.filter(start_at__gt=datetime.now())
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'category': request.data.get('category'),
            'city': request.data.get('city'),
            'price': request.data.get('price'),
            'start_at': request.data.get('start_at'),
            'link': request.data.get('link'),
            'picture': request.data.get('picture'),
            'description': request.data.get('description'),
            'user_creator': request.user,

        }
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetailApiView(APIView):

    permission_classes = [permissions.IsAdminUser]

    def get_object(self, event_id):

        try:
            return Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return None

    def get(self, request, event_id, *args, **kwargs):

        event_instance = self.get_object(event_id)
        if not event_instance:
            return Response(
                {"res": "Object with event id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = EventSerializer(event_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, event_id, *args, **kwargs):

        event_instance = self.get_object(event_id)
        if not event_instance:
            return Response(
                {"res": "Object with event id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'category': request.data.get('category'),
            'city': request.data.get('city'),
            'price': request.data.get('price'),
            'start_at': request.data.get('start_at'),
            'link': request.data.get('link'),
            'picture': request.data.get('picture'),
            'description': request.data.get('description'),
            'user_creator': request.user,
        }
        serializer = EventSerializer(instance = event_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, event_id, *args, **kwargs):

        event_instance = self.get_object(event_id)
        if not event_instance:
            return Response(
                {"res": "Object with event id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        event_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


def detail_api_view(request):
    if request.method == 'POST':
        try:
            pk = request.POST.get('id')
            event = Event.objects.filter(id=pk)
            if event:
                return redirect(f'/api/{pk}/')
            else:
                messages.error(request, "Cant find your event API.")
        except:
            messages.error(request, "Select valid ID")
    return render(request, 'get_events_API.html')

