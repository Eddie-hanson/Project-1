from django.db import models

# Create your models here.
#destination class
class Destination(models.Model):
    #id=models.IntegerField()
    Name= models.CharField(max_length=100 )
    img = models.ImageField(upload_to= 'pics' )
    desc= models.TextField()
    Price = models.IntegerField()
    offer= models.BooleanField(default= False )
    def __str__(self):
        return self.Name
class bestTrips(models.Model):
    day=models.IntegerField()
    month=models.CharField(max_length= 15)
    desc=models.TextField()
    img=models.ImageField(upload_to='pics')
        
class Subscription(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    
class Available_Trips(models.Model)  : 
    Name= models.CharField(max_length=100 )
    img = models.ImageField(upload_to= 'pics' )
    desc= models.TextField()
    Price = models.IntegerField()
    offer= models.BooleanField(default= False )
    date= models.DateField
    def __str__(self):
        return self.Name





# class Flight(models.Model):
#     origin_city = models.CharField(max_length=100)
#     destination_city = models.CharField(max_length=100)
#     arrival_time = models.DateTimeField()
#     budget = models.DecimalField(max_digits=10, decimal_places=2)
   
    

