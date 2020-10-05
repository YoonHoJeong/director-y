# Generated by Django 2.2.14 on 2020-10-05 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('title_eng', models.CharField(blank=True, max_length=30)),
                ('poster', models.ImageField(upload_to='')),
                ('trailer', models.URLField(blank=True)),
                ('trailer_thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('genre', models.CharField(max_length=20)),
                ('summary', models.TextField()),
                ('production_year', models.PositiveIntegerField()),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SPortfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('thumbnail', models.TextField()),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='')),
                ('mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('award_category', models.CharField(max_length=50)),
                ('award_title', models.CharField(max_length=50)),
                ('mid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='ActorVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.URLField()),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Actor')),
            ],
        ),
        migrations.CreateModel(
            name='ActorImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('aid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Actor')),
            ],
        ),
    ]
