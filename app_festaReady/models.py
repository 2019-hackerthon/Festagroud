from django.db import models

# Create your models here.
class Accompany(models.Model) : #festa_ready의 동행구하는 게시판
    title = models.CharField(max_length=200) 
    writer = models.CharField(max_length=200) 
    area = models.CharField(max_length=200) 
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
    title = models.CharField(max_length=200) #제목
    writer = models.CharField(max_length=200) #작성자
    deal_type = models.CharField(max_length=200) #양도/교환
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