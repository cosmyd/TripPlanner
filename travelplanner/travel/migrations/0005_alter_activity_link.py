# Generated by Django 5.0.2 on 2024-03-11 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_trip_users_alter_trip_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
