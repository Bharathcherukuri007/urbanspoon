# Generated by Django 3.1.7 on 2021-05-07 07:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_doctoradvice_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default=datetime.datetime(2021, 5, 7, 7, 32, 38, 633402, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
