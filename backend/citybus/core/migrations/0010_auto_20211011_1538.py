# Generated by Django 3.2.8 on 2021-10-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20211011_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='latitude',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='longitude',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True),
        ),
    ]
