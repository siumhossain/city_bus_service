# Generated by Django 3.2.8 on 2021-11-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_applyhalf'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applyhalf',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='applyhalf',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
