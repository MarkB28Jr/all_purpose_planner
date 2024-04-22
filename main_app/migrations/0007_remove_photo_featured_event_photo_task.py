# Generated by Django 5.0.4 on 2024-04-22 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='featured_event',
        ),
        migrations.AddField(
            model_name='photo',
            name='task',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main_app.task'),
        ),
    ]
