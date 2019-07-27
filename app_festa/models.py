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
    class Meta :
        ordering = ['schedule'] #가장 빠른 festa부터 게시

#ready
class Accompany(models.Model) : #festa_ready의 동행구하는 게시판
    title = models.CharField(max_length=200) 
    writer = models.CharField(max_length=200) 
    area = models.CharField(max_length=200) 
    password = models.CharField(max_length=20)
    description = models.TextField() 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Commenta(models.Model):
    writer_accompany = models.CharField(max_length=200)
    content_accompany = models.TextField()
    accompany = models.ForeignKey(Accompany, on_delete=models.CASCADE)



class Ticket(models.Model): #festa_ready의 티켓 양도 교환 게시판
    title = models.CharField(max_length=200) #제목
    writer = models.CharField(max_length=200) #작성자
    deal_type = models.CharField(max_length=200) #양도/교환
    password = models.CharField(max_length=20)
    description = models.TextField() #내용

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Commenttic(models.Model):
    writer_ticket = models.CharField(max_length=200)
    content_ticket = models.TextField()
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)


class Now(models.Model):

    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    password = models.CharField(max_length=20)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]


class Team(models.Model):

    title2 = models.CharField(max_length=200)
    writer2 = models.CharField(max_length=100)
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
    title = models.CharField(max_length=200) #글제목
    writer = models.CharField(max_length=200) #작성자
    region = models.CharField(max_length=200) #지역
    body = models.TextField() #내용
    pub_date = models.DateTimeField('date published')
    
class RegisterNum(models.Model) :
    register_num = models.CharField(max_length = 10)

    def __str__(self) :
        return self.register_num



