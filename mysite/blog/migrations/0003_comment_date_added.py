# Generated by Django 2.0.4 on 2018-04-26 19:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180426_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
