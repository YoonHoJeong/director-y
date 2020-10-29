from django.db import models
from accounts.models import Profile, Director, Actor, Staff
# Create your models here.

# Director's Portfolio


class Movie(models.Model):
    """ 
        Fields
            1. title(kor) - CharField
            2. title(eng) - CharField
            3. poster - ImageField
            4. trailer - URLField
            5. trailer-thumbnail- ImageField
            6. genre - CharField
            7. summary - TextField
    """
    uid = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=30, blank=False, null=False)
    title_eng = models.CharField(max_length=30, blank=True)
    poster = models.ImageField(blank=False, null=False)
    trailer = models.URLField(blank=True)
    trailer_thumbnail = models.ImageField(null=True, blank=True)
    genre = models.CharField(max_length=20, blank=False)
    summary = models.TextField(blank=False)
    production_year = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return self.title
#   영화제
#   한 영화제에서 1개의 상만 탈 수 있다고 가정.


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
    """ 
        portfolio id

        content
            - image
            - text
            - video(undefined)
            - 
    """
    mid = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, blank=False)
    thumbnail = models.ImageField(null=True, blank=True)
    content = models.TextField(default="")

    def __str__(self):
        return self.title

# Staff's Portfolio


class SPortfolio(models.Model):
    """ 
        Fields
            1. 

    """
    uid = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, blank=False)
    thumbnail = models.TextField(blank=False, null=False)
    # content : smart editor에서 제공.

    def __str__(self):
        return self.title


class ActorImage(models.Model):
    aid = models.ForeignKey(Actor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class ActorVideo(models.Model):
    pid = models.ForeignKey(Actor, on_delete=models.CASCADE)
    video_url = models.URLField()
