from django.db import models

# Create your models here.
class Festa(models.Model) :
    name = models.CharField(max_length = 200)
    schedule = models.DateField('date published')
    space = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'images/%Y/%m/%d')

    def __str__(self) :
        return self.name