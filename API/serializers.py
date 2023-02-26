from rest_framework import serializers

from EventViewer.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'category', 'city', 'price', 'start_at',
                  'link', 'picture', 'description']