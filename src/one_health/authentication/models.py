
from django.db import models

from django.contrib.auth.models import AbstractUser
#from phonenumber_field.modelfields import PhoneNumberField

# class SocialLink(models.Model):
#     name = models.CharField(max_length=30)
#     icon =   models.CharField(max_length=30)
#     link =  models.URLField()

class User(AbstractUser):
    
    
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='doctors_img')
    number = models.CharField(max_length=15)
    service = models.CharField(max_length=50)
    def __str__(self):
        return self.username
    

#class Doctor(User):
    
    
    
    
