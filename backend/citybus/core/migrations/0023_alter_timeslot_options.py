# Generated by Django 3.2.8 on 2021-11-02 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_album_track'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timeslot',
            options={'ordering': ['bus_name', 'trip_number', 'station_serial', 'time']},
        ),
    ]
