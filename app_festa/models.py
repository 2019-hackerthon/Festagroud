from django.db import models

# Create your models here.
class Festa(models.Model) :
    name = models.CharField(max_length = 200) #공연이름
    schedule = models.DateField('date published') #공연날짜
    space = models.CharField(max_length = 200) #공연장소
    info = models.TextField() #공연상세정보
    image = models.ImageField(upload_to = 'images/%Y/%m/%d') #공연포스터

    def __str__(self) :
        return self.name