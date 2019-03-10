# Generated by Django 2.1 on 2019-03-10 01:31

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_authenticator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authenticator',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 3, 10, 1, 31, 23, 305107, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='authenticator',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Seller'),
        ),
    ]
