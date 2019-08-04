from django.db import models
from app_festa.models import Festa

# Create your models here.
class Accompany(models.Model) : #festa_ready의 동행구하는 게시판
    festa = models.ForeignKey(Festa, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) 
    writer = models.CharField(max_length=200) 
    AREA = (
        ('서울', '서울'),
        ('경기', '경기'),
        ('강원', '강원'),
        ('충남', '충남'),
        ('충북', '충북'),
        ('경북', '경북'),
        ('경남', '경남'),
        ('전북', '전북'),
        ('전남', '전남'),
        ('제주', '제주'),
    )
    area = models.CharField(max_length=200, choices = AREA) 
    password = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to = "images/", null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Commenta(models.Model):
    writer_accompany = models.CharField(max_length=200)
    content_accompany = models.TextField()
    password = models.CharField(max_length=20)
    accompany = models.ForeignKey(Accompany, on_delete=models.CASCADE)


class Ticket(models.Model): #festa_ready의 티켓 양도 교환 게시판
    festa = models.ForeignKey(Festa, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) #제목
    DEAL_TYPE = (
        ('양도해요', '양도해요'),
        ('양도받아요', '양도받아요'),
        ('교환해요', '교환해요'),
    )
    deal_type = models.CharField(max_length=200, choices = DEAL_TYPE) #양도/교환
    writer = models.CharField(max_length=200) #작성자
    password = models.CharField(max_length=20)
    description = models.TextField() #내용
    image = models.ImageField(upload_to =  "images/", null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Commenttic(models.Model):
    writer_ticket = models.CharField(max_length=200)
    content_ticket = models.TextField()
    password = models.CharField(max_length=20)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)