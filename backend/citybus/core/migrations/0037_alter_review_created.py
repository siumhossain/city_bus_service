# Generated by Django 3.2.8 on 2021-11-17 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.TimeField(auto_now=True),
        ),
    ]