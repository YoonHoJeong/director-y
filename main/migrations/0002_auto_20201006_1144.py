# Generated by Django 2.2.14 on 2020-10-06 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='mid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Movie'),
        ),
    ]