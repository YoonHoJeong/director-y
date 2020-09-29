from django.db import models
from accounts.models import Profile, Director, Actor, Staff
# Create your models here.


class Portfolio(models.Model):
    """
        one(Portfolio) - many(Section) 관계.

        title

        uid
            - 작성한 유저의 아이디.
            - Profile(one) - portfolio(many) 관계.
            - Portfolio에서 foreign key로 연결한다.
    """
    # uid = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# Director's Portfolio


class DPortfolio(Portfolio):
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
    uid = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    title_kor = models.CharField(max_length=30, blank=False)
    title_eng = models.CharField(max_length=30, blank=False)
    poster = models.ImageField(null=True, blank=False)
    trailer = models.URLField(blank=True)
    trailer_thumbnail = models.ImageField(null=True, blank=True)
    genre = models.CharField(max_length=20, blank=False)
    summary = models.TextField(blank=False)


# Actor's Portfolio
class APortfolio(Portfolio):
    """ 
        Fields
            1. image - ImageField
            2. Filmography - TextField
            3. video-title - CharField
            4. video-url - URLField

    """
    uid = models.ForeignKey(Actor, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)
    Filmography = models.TextField(null=True, blank=False)
    video_title = models.CharField(max_length=20, null=True, blank=False)
    video_url = models.URLField(null=True, blank=False)
# Staff's Portfolio


class SPortfolio(Portfolio):
    """ 
        Fields
            1. 

    """
    uid = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)


class Section(models.Model):
    """ 
        portfolio id

        content
            - image
            - text
            - video(undefined)
            - 
    """
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='images/')


class PortfolioImage(models.Model):
    pid = models.ForeignKey(APortfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class PortfolioVideo(models.Model):
    pid = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    video_link = models.URLField()
