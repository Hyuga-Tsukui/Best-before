# Generated by Django 3.1.1 on 2020-09-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0005_remove_food_memo'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='note',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
