# Generated by Django 3.2.8 on 2021-10-11 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211011_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='seat_number',
            field=models.CharField(default='', max_length=10),
        ),
    ]