# Generated by Django 4.1.6 on 2023-02-26 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventViewer', '0008_alter_event_user_attend'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-start_at']},
        ),
        migrations.AlterField(
            model_name='event',
            name='end_at',
            field=models.DateTimeField(null=True),
        ),
    ]
