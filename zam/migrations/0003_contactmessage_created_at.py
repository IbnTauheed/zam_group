# Generated by Django 5.1.4 on 2025-01-27 21:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zam', '0002_contactmessage_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
