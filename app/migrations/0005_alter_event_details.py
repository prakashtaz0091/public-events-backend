# Generated by Django 4.1.5 on 2023-01-23 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_event_date_alter_event_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='details',
            field=models.TextField(blank=True),
        ),
    ]