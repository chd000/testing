# Generated by Django 3.1 on 2020-08-15 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0010_auto_20200814_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='working_at',
        ),
        migrations.RemoveField(
            model_name='resulttable',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='resulttable',
            name='passing_test_date',
        ),
    ]
