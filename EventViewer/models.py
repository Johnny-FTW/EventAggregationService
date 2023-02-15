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
    end_at = DateTimeField()
    link = CharField(max_length=200)
    picture = CharField(max_length=200)
    description = TextField(max_length=1024)
    user = ManyToManyField(User, related_name='attending')
    title_photo = CharField(max_length=200, null=True)
    #attending

    def __str__(self):
        return self.name


# class comment
