# Generated by Django 3.2.8 on 2021-11-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_alter_announcement_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
