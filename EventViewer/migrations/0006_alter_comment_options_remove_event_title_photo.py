# Generated by Django 4.1.6 on 2023-02-16 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventViewer', '0005_alter_event_user_attend'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created', 'user']},
        ),
        migrations.RemoveField(
            model_name='event',
            name='title_photo',
        ),
    ]
