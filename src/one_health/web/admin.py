from django.contrib import admin
from django.utils.safestring import mark_safe
from web.models import *

# Register your models here.
@admin.register(About)
class AdminAbout(admin.ModelAdmin):
    list_display = [
        "img_about",
        "title_about",
        "description_about",
        "active"]
    def img_about(self, obj): 
        return mark_safe(f'<img src="{obj.image_about.url}" style="height:100px; width:200px">')

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = [
        "name_contact","email_contact","subject_contact","active"
    ]

@admin.register(SocialLink)
class AdminSocialLinkt(admin.ModelAdmin):
    list_display = [
        "name_link","icon_link","link_link","active"
    ]
 
@admin.register(SiteInfos)
class AdminSite(admin.ModelAdmin):
    list_display = [
        "name_site",
        "email_site",
        "phone_site",
        "address_site",
        "media_social",
        "copyright_site",
        "active"]

@admin.register(Banner)
class AdminBanner(admin.ModelAdmin):
    list_display =[
        "image_banner","label1","label2","active"
    ]
    def image_banner(self, obj): 
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')
