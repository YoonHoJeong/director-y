# Generated by Django 3.1.3 on 2020-11-30 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_merge_20201130_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportfolio',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
