from django.db import models

# Create your models here.
class Festa(models.Model) :
    name = models.CharField(max_length = 200) #공연제목
    schedule = models.DateField('date published') #공연날짜
    space = models.CharField(max_length = 200) #공연장소
    purchase_link = models.CharField(max_length = 200) #공식 티켓판매처 링크
    host = models.CharField(max_length = 200) #공연 주최/기획사
    contact = models.CharField(max_length = 200) #고객 문의처
    precautions = models.TextField() #유의사항
    notice = models.TextField() #공지사항
    poster = models.ImageField(upload_to = 'images/%Y/%m/%d') #공연포스터

    def __str__(self) :
        return self.name