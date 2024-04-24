# Generated by Django 5.0.4 on 2024-04-24 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_featuredevent_city_featuredevent_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featuredevent',
            name='featuredEvents',
        ),
        migrations.RemoveField(
            model_name='task',
            name='image_url',
        ),
        migrations.AddField(
            model_name='task',
            name='featuredevents',
            field=models.ManyToManyField(to='main_app.featuredevent'),
        ),
    ]
