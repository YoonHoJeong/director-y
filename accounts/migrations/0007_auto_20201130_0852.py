# Generated by Django 2.2.14 on 2020-11-29 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='type',
            field=models.IntegerField(choices=[(1, 'movie'), (2, 'director'), (3, 'actor'), (4, 'staff')]),
        ),
    ]
