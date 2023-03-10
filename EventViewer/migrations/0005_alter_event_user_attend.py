# Generated by Django 4.1.6 on 2023-02-16 16:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EventViewer', '0004_alter_event_options_alter_event_user_attend_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='user_attend',
            field=models.ManyToManyField(related_name='attending_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
