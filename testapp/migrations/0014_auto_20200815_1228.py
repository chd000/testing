# Generated by Django 3.1 on 2020-08-15 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0013_auto_20200815_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(max_length=100, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='resulttable',
            name='middle_name',
            field=models.CharField(max_length=100, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='resulttable',
            name='passing_test_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата прохождения теста'),
        ),
    ]
