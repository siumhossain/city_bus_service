# Generated by Django 3.2.8 on 2021-10-11 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_buses_seat_each_row'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='deprature_point',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='ticket',
            name='destination',
            field=models.CharField(default='', max_length=50),
        ),
    ]
