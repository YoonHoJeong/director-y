from django.db import models

# Create your models here.


class Portfolio(models.Model):
    """
        section_list : 하위 섹션들에 대한 값을 갖고 있음.
        -> Section model에서 foreign key로 연결한다.
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
