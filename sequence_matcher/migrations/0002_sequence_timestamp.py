# Generated by Django 3.0.2 on 2020-01-20 16:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sequence_matcher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequence',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
