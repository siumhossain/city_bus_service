# Generated by Django 3.2.8 on 2021-11-16 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20211116_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyhalf',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
    ]
