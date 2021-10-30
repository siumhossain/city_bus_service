# Generated by Django 3.2.8 on 2021-10-12 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_timeslot_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslot',
            name='station_serial',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Routes',
        ),
    ]
