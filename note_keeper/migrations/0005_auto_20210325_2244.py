# Generated by Django 3.1.7 on 2021-03-25 15:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('note_keeper', '0004_auto_20210316_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='id',
        ),
        migrations.AlterField(
            model_name='note',
            name='doc',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 15, 44, 32, 765799, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='note',
            name='modify_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 15, 44, 32, 765828, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
