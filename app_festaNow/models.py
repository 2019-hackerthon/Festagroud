from django.db import models
from app_festa.models import Festa


# Create your models here.
class Now(models.Model):
    festa = models.ForeignKey(Festa, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    POST_TYPE = (
        ('now', 'now'),
        ('질문', '질문'),
        ('나눔', '나눔'),
    )
    post_type = models.CharField(max_length = 100, choices = POST_TYPE)
    pub_date = models.DateTimeField('date published')
    password = models.CharField(max_length=20)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


class Team(models.Model):
    festa = models.ForeignKey(Festa, on_delete=models.CASCADE)
    title2 = models.CharField(max_length=200)
    writer2 = models.CharField(max_length=100)
    POST_TYPE = (
        ('중요', '중요'),
        ('질문', '질문'),
    )
    post_type = models.CharField(max_length = 100, choices = POST_TYPE)
    pub_date2 = models.DateTimeField('date published')
    password2 = models.CharField(max_length=20)
    body2 = models.TextField()

    def __str__(self):
        return self.title2

    def summary(self):
        return self.body2[:100]


class Commentn(models.Model):
    writer_now = models.CharField(max_length=200)
    content_now = models.TextField()
    now = models.ForeignKey(Now, on_delete=models.CASCADE)

class Commentt(models.Model):
    writer_team = models.CharField(max_length=200)
    content_team = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

##집가자 게시판

class Home(models.Model) : #festa_ready의 동행구하는 게시판
    festa = models.ForeignKey(Festa, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #글제목
    writer = models.CharField(max_length=200) #작성자
    REGION = (
        ('서울', '서울'),
        ('경기', '경기'),
        ('제주', '제주'),
    )
    region = models.CharField(max_length=200, choices = REGION ) #지역
    body = models.TextField() #내용
    pub_date = models.DateTimeField('date published')
    

class Commenth(models.Model):
    writer_home = models.CharField(max_length=200)
    content_home = models.TextField()
    home = models.ForeignKey(Home, on_delete=models.CASCADE)


class ReservationNum(models.Model) :
    reservation_name = models.CharField(max_length = 30)
    reservation_num = models.CharField(max_length = 30)
    festa = models.ForeignKey(Festa, on_delete=models.CASCADE)
    def __str__(self) :
        return self.reservation_name

    def __str__(self) :
        return self.reservation_num