# Generated by Django 4.2.7 on 2023-11-30 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
