# Generated by Django 3.1.1 on 2020-09-25 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_food_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='memo',
            field=models.TextField(null=True),
        ),
    ]