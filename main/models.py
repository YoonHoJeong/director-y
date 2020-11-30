from django.db import models
from accounts.models import Profile, Director, Actor, Staff
# Create your models here.

# Director's Portfolio


class Movie(models.Model):
    genres = ["액션","범죄","SF","코미디","스릴러","전쟁","스포츠","판타지","음악","멜로"]

    GENRE_CHOICES = ((genre, genre) for genre in genres)

    director = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=30, blank=False, null=False)
    title_eng = models.CharField(max_length=30, blank=True)
    poster = models.ImageField(upload_to = 'images/', blank=False, null=False)
    trailer = models.URLField(blank=True)
    trailer_thumbnail = models.ImageField(null=False, default=None)
    genre = models.CharField(choices = GENRE_CHOICES, max_length=20, blank=False)
    summary = models.TextField(blank=False)
    production_year = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return self.title


class Festival(models.Model):
    mid = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50, blank=False)
    year = models.PositiveIntegerField()
    award_category = models.CharField(max_length=50)
    award_title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

#   Movie - Section

class Section(models.Model):
    mid = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, blank=False)
    thumbnail = models.ImageField(null=True, blank=True)
    content = models.TextField(default="")

    def __str__(self):
        return self.title

# Staff's Portfolio

class SPortfolio(models.Model):
    uid = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, blank=False)
    thumbnail = models.ImageField(null=True, blank=True)
    content = models.TextField(default="")

def __str__(self):
        return self.title

class ActorImage(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class ActorVideo(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    video_url = models.URLField()

class Genre(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Filmography(models.Model):
    # movie - profile 연걸 many-to-many
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)


    def __str__(self):
        return self.profile.name + " / " + self.movie.title + " / " + self.role
