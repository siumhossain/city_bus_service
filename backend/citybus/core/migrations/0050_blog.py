# Generated by Django 3.2.8 on 2021-11-23 17:43

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_alter_announcement_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('short_description', models.TextField()),
                ('content', tinymce.models.HTMLField()),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
