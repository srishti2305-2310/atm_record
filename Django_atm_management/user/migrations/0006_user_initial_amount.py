# Generated by Django 5.0.7 on 2024-07-25 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='initial_amount',
            field=models.IntegerField(default=0),
        ),
    ]
