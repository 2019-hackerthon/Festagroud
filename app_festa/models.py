from django.db import models

# Create your models here.
class RegisterNum(models.Model) :
    register_num = models.CharField(max_length = 10)

    def __str__(self) :
        return self.register_num

class Festa(models.Model) :
    number = models.OneToOneField(RegisterNum, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200) #공연제목
    schedule = models.DateField('date published') #공연날짜
    space = models.CharField(max_length = 200) #공연장소
    purchase_link = models.CharField(max_length = 200) #공식 티켓판매처 링크
    host = models.CharField(max_length = 200) #공연 주최/기획사
    contact = models.CharField(max_length = 200) #고객 문의처
    detail_map = models.CharField(max_length = 200) #지도(상세주소)
    precautions = models.TextField() #유의사항
    notice = models.TextField() #공지사항
    poster = models.ImageField(upload_to = 'images/%Y/%m/%d') #공연포스터

    def __str__(self) :
        return self.name
    class Meta :
        ordering = ['schedule'] #가장 빠른 festa부터 게시


class Staff(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    festa = models.ForeignKey(Festa, on_delete=models.CASCADE)

class Audience(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()