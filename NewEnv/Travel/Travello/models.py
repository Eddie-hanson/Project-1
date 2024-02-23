from django.db import models

# Create your models here.
#destination class
class Destination(models.Model):
    id:int
    Name= models.CharField(max_length=100 )
    img = models.ImageField(upload_to= 'pics' )
    desc= models.TextField
    Price = models.IntegerField
    offer= models.BooleanField(default= False )
    

