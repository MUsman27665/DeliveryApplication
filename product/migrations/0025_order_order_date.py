# Generated by Django 3.1.2 on 2020-11-02 11:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_auto_20201102_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.date(2020, 11, 2)),
        ),
    ]
