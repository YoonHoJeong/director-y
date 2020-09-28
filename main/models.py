from django.db import models

# Create your models here.


class Portfolio(models.Model):
    """
        one(Portfolio) - many(Section) 관계.

        title

        uid
            - 작성한 유저의 아이디.
            - user(one) - portfolio(many) 관계.
            - Portfolio에서 foreign key로 연결한다.
    """
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

# Actor's Portfolio


class APortfolio(Portfolio):
    """ 
        Fields
            1. image - ImageField
            2. Filmography - TextField
            3. video-title - CharField
            4. video-url - URLField

    """

# Staff's Portfolio


class SPortfolio(Portfolio):
    """ 
        Fields
            1. 

    """


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
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
