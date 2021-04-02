# Generated by Django 3.1.7 on 2021-03-28 07:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('note_keeper', '0013_auto_20210328_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='doc',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 7, 16, 10, 16158, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='note',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 28, 7, 16, 10, 16158, tzinfo=utc), verbose_name='date published'),
        ),
    ]