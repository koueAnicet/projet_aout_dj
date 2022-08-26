
from django.db import models

from django.contrib.auth.models import AbstractUser
#from phonenumber_field.modelfields import PhoneNumberField

# class SocialLink(models.Model):
#     name = models.CharField(max_length=30)
#     icon =   models.CharField(max_length=30)
#     link =  models.URLField()

class User(AbstractUser):
    DOCTOR = 'DOCTOR'
    PATIENT = 'PATIENT'
    ROLE = (
        (DOCTOR, 'Docteur'),
        (PATIENT, 'Patient'),
    )
    photo = models.ImageField(upload_to='doctors_img')
    role = models.CharField(choices=ROLE, max_length=30, verbose_name='Rôle')
    service = models.CharField(max_length=50, blank=True, null=True)
    #telephone_number = PhoneNumberField(unique=False, region="CI")
    def __str__(self):
        return self.username
    
    
    
