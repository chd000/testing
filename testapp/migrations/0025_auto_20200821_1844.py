# Generated by Django 3.1 on 2020-08-21 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0024_questions_answered_wrong'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='picture',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='static/media/', verbose_name='Изображения'),
        ),
    ]
