# Generated by Django 5.0.2 on 2024-03-05 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travel.trip'),
        ),
    ]
