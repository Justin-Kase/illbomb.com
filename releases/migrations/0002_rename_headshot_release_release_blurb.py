# Generated by Django 4.0.1 on 2022-01-24 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('releases', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='release',
            old_name='headshot',
            new_name='release_blurb',
        ),
    ]
