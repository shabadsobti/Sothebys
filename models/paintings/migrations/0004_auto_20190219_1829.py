# Generated by Django 2.1 on 2019-02-19 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0003_painting_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 19, 18, 29, 3, 627079)),
        ),
    ]