# Generated by Django 2.2.14 on 2020-11-13 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201113_1528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actorimage',
            old_name='aid',
            new_name='actor',
        ),
        migrations.RenameField(
            model_name='actorvideo',
            old_name='pid',
            new_name='actor',
        ),
    ]