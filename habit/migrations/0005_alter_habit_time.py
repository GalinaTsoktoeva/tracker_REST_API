# Generated by Django 4.2.4 on 2023-08-27 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0004_alter_habit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 27, 17, 46, 27, 760219), verbose_name='время'),
        ),
    ]