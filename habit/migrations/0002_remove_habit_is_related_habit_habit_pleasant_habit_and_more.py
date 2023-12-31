# Generated by Django 4.2.4 on 2023-08-26 15:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='is_related_habit',
        ),
        migrations.AddField(
            model_name='habit',
            name='pleasant_habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habit', to='habit.habit', verbose_name='приятная привычка'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.PositiveSmallIntegerField(choices=[(1, 'каждый день'), (2, 'раз в два дня'), (3, 'раз в три дня'), (4, 'раз в четыре дня'), (5, 'раз в пять дней'), (6, 'раз в шесть дней'), (7, 'раз в семь дней')], default=1, verbose_name='периодичность'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 26, 18, 46, 56, 785164), verbose_name='время'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habit', to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]
