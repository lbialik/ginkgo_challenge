# Generated by Django 3.0.2 on 2020-01-17 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('protein', models.TextField()),
                ('index', models.CharField(max_length=20)),
            ],
        ),
    ]
