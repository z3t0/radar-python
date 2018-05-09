from .models import Society, Event
from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'description', 'start_time', 'end_time',
                  'location', 'society')


class SocietySerializer(serializers.HyperlinkedModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Society
        fields = ('name', 'description', 'events')
