# Generated by Django 3.1.7 on 2021-03-26 05:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('note_keeper', '0010_auto_20210326_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='doc',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 5, 13, 6, 549631, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='note',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 5, 13, 6, 549631, tzinfo=utc), verbose_name='date published'),
        ),
    ]
