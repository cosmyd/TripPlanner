# Generated by Django 5.0.2 on 2024-03-06 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_activity_trip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
