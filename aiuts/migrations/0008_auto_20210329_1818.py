# Generated by Django 3.1.7 on 2021-03-29 11:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aiuts', '0007_auto_20210329_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='record_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 29, 11, 18, 16, 425792, tzinfo=utc), verbose_name='date recorded'),
        ),
    ]
