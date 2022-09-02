from django.utils.safestring import mark_safe
from django.contrib import admin
from service.models import *

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display=[
        "image","title","description","active"
    ]

@admin.register(Testimonial)
class AdminTestimonial(admin.ModelAdmin):
    list_display=["name","email","website","active"]



@admin.register(SocialLinkDoctor)
class AdminSocialLinkDoctor(admin.ModelAdmin):
    list_display = [
        "name_link","icon_link","link_link","active"
    ]

@admin.register(Departement)
class AdminAppointment(admin.ModelAdmin):
    list_display=[
        "name_department","active"  
    ]

@admin.register(Appointment)
class AdminAppointment(admin.ModelAdmin):
    list_display=[
        "full_name","email_address","department",
        "birthday","number","message","active"
    ]
@admin.register(Doctor)
class AdminDoctor(admin.ModelAdmin):
    list_display=[
        "img_doctor","name",
        "spaciality","social_media","active"
    ]
    def img_doctor(self, obj): 
            return mark_safe(f'<img src="{obj.photo.url}" style="height:100px; width:200px">')

    



