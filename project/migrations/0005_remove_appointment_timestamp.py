# Generated by Django 3.1.7 on 2021-05-05 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20210505_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='timestamp',
        ),
    ]