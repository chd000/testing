# Generated by Django 3.1 on 2020-08-21 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0023_auto_20200820_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='answered_wrong',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Неправильно ответили раз'),
        ),
    ]
