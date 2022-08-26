from django.conf import settings
from django.db import models
from django.contrib.auth.models import User



class Testimonial(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    website = models.URLField(null=True, blank=None)
    active = models.BooleanField()
    
    def __str__(self):
        return self.name


class Blog(models.Model):
    tag = models.CharField(max_length=30)
    image = models.ImageField(upload_to='blog_img')    
    title = models.CharField(max_length=50)
    description = models.TextField()
    active = models.BooleanField()
    def __str__(self):
        return self.title
    
class SocialLinkDoctor(models.Model):
    name_link = models.CharField(max_length=15)
    icon_link = models.CharField(max_length=50)
    link_link = models.URLField(max_length=100)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name_link
    
    
class Speciality(models.Model):
    speciality = models.CharField(max_length=100)
    def __str__(self):
        return self.Speciality  
class Departement(models.Model):
    name_department = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name_department   
      
class Doctor(models.Model):
    
    photo = models.ImageField(upload_to="doctor_imgs")
    name = models.CharField(max_length=30)
    spaciality = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True)
    social_media = models.ForeignKey(SocialLinkDoctor, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Ville(models.Model):
    nom_ville = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nom_ville
 
class Horaire(models.Model):
    horaire = models.TimeField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.horaire
    
class Jours(models.Model):
    jours = models.DateField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.jours
     
class Consultation(models.Model):
    doctor_cons = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    tarif = models.CharField(max_length=10)
    ville = models.ForeignKey(Ville, on_delete=models.SET_NULL, null=True)
    horaires = models.ForeignKey(Horaire, on_delete=models.SET_NULL, null=True)
    jours = models.ForeignKey(Jours, on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.doctor_cons
    
    

    
    
class Appointment(models.Model):
    full_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=50)
    department = models.ForeignKey(Departement, on_delete=models.CASCADE)
    birthday = models.CharField(max_length=10)
    number = models.CharField(max_length=15)
    message = models.TextField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.full_name
        
class Convention(Appointment, Testimonial, Blog, Doctor):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True