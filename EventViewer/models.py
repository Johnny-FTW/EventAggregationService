from django.contrib.auth.models import User
from django.db import models
from django.db.models import *


# Create your models here.


class Category(Model):
    name = CharField(max_length=50)

    def __str__(self):
        return self.name

class Event(Model):
    name = CharField(max_length=50)
    category = ForeignKey(Category, on_delete=DO_NOTHING)
    city = CharField(max_length=50)
    price = FloatField()
    start_at = DateTimeField()
    end_at = DateTimeField(null=True)
    link = CharField(max_length=200)
    picture = CharField(max_length=200)
    description = TextField(max_length=1024)
    user_attend = ManyToManyField(User, related_name='attending_user', blank=True)
    user_creator = ForeignKey(User, on_delete=DO_NOTHING, null=True)

    class Meta:
        ordering = ['-start_at']

    def __str__(self):
        return self.name


class Comment(Model):
    event = ForeignKey(Event, null=False, on_delete=CASCADE, related_name='event_comment')
    user = ForeignKey(User, null=False, on_delete=CASCADE, related_name='user_comment')
    comment = TextField(null=False)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', 'user']

    def __str__(self):
        return f'Event {self.event} commented by {self.user}'

