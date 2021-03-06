# Generated by Django 3.1.7 on 2021-03-27 03:12

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aiuts', '0003_auto_20210326_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('amount', models.FloatField()),
                ('record_date', models.DateTimeField(default=datetime.datetime(2021, 3, 27, 3, 12, 7, 11670, tzinfo=utc), primary_key=True, serialize=False, verbose_name='date recorded')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipient', to='aiuts.user')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='aiuts.user')),
            ],
        ),
    ]
