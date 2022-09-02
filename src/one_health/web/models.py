from django.db import models
from tinymce.models import HTMLField

class About(models.Model):
    title_about = models.CharField(max_length=150)
    description_about = HTMLField()
    image_about = models.ImageField(upload_to='about_img')
    active = models.BooleanField(default=True)
    def __str__(self)-> str:
        return self.title_about
    

class Contact(models.Model):
    name_contact =  models.CharField(max_length=30)
    email_contact = models.EmailField()
    subject_contact = models.TextField()
    message =models.TextField()
    active = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name_contact

class SocialLink(models.Model):
    name_link = models.CharField(max_length=15)
    icon_link = models.CharField(max_length=50)
    link_link = models.URLField(max_length=100)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name_link
    

class SiteInfos(models.Model):
    name_site = models.CharField(max_length=50)
    email_site = models.EmailField(blank=True, null=True)
    phone_site = models.CharField(max_length=15, 
        blank=True, null=True)
    address_site = models.CharField(max_length=50)
    media_social = models.ForeignKey(SocialLink,
        on_delete=models.SET_NULL,  
        blank=True, null=True)
    copyright_site = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name_site
    
class Banner(models.Model):
    image = models.ImageField(upload_to='banner_img')
    label1 = models.CharField(max_length=100, blank=True, null=True)
    label2 = models.CharField(max_length=100,  blank=True, null=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.label1
    