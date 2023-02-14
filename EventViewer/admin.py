from django.contrib import admin

from EventViewer.models import Event, Category

# Register your models here.

admin.site.register(Event)
admin.site.register(Category)
