# Generated by Django 2.2.14 on 2020-11-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20201130_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='type',
            field=models.IntegerField(choices=[(0, 'movie'), (1, 'director'), (2, 'actor'), (3, 'staff')]),
        ),
    ]