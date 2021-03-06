# Generated by Django 3.1 on 2020-08-14 08:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_auto_20200810_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(default='none', max_length=100, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='working_at',
            field=models.CharField(blank=True, choices=[('GA-36', 'ГА-36'), ('GAC', 'ГАЦ'), ('CSU', 'ЦСЮ')], max_length=50, verbose_name='Место работы'),
        ),
        migrations.AddField(
            model_name='resulttable',
            name='middle_name',
            field=models.CharField(default='none', max_length=100, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='resulttable',
            name='passing_test_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата прохождения теста'),
            preserve_default=False,
        ),
    ]
