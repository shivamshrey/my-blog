# Generated by Django 3.2.4 on 2021-06-24 09:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210624_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 24, 9, 28, 40, 249035, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 24, 9, 28, 40, 248369, tzinfo=utc)),
        ),
    ]
