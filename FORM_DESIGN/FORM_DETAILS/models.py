from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    sdesc = models.CharField(max_length=100)
    detail= models.CharField(max_length=500)
    category = models.IntegerField()
    FirstName = models.CharField(max_length=10)
    LastName= models.TextField(max_length=30)
    gender = models.TextField()
    country_code = models.IntegerField()
    Mobile_No = models.CharField(max_length=50)
    Emailid = models.EmailField(max_length=50)
    password = models.IntegerField(75)
    cpassword = models.IntegerField(75)
    isactive = models.IntegerField()
    
    def __str__(self):
        return self.title
    
   
