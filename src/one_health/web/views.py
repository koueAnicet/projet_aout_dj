from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from authentication.models import User
from service.models import Departement
from web import models as webmodels
from service import models

import requests
import json

URLS = "https://newsapi.org/v2/everything?q=medical&from=2022-07-27&sortBy=publishedAt&apiKey=bd48bd00db6d4feab29c5a6aa5582cd0"


class PageHomeView(View):
    template_name = "one_health/index.html"
    alert =""
    success = True 
    
    def get(self, request):
        about = webmodels.About.objects.first()
        doctors = models.Doctor.objects.all()
        banner = webmodels.Banner.objects.first()
        departments = models.Departement.objects.all()
        
        #----------API---------------#

        resul = requests.get(URLS)
        data = json.loads(resul.text)

        totalResult = data['totalResults']
        articles= data['articles'][:3]
        
        return render(request, self.template_name, locals())
    
    def post(self, request):
        full_name = request.POST.get('name')
        email_address = request.POST.get('adresse')
        pk_department = request.POST.get('departement')
        department = get_object_or_404(Departement, pk=pk_department)
        birthday = request.POST.get('date')
        number = request.POST.get('number')
        message = request.POST.get('message')
        
        appointment = models.Appointment.objects.create(
            full_name=full_name,
            email_address=email_address,
            department=department,
            birthday=birthday,
            number=number,
            message=message,
        )
       
        data={
            'alert': self.alert,
            'success':self.success,
            }
        return render(request, self.template_name, locals())
    


class PageDoctorView(View):
    template_name ="one_health/doctors.html"
    
    alert =""
    success = True 
    
    def get(self, request):
        departments = models.Departement.objects.all()
        doctors = models.Doctor.objects.all()
        return render(request,self.template_name, locals())
    
    def post(self, request):
        full_name = request.POST.get('name')
        email_address = request.POST.get('adresse')
        pk_department = request.POST.get('departement')
        department = get_object_or_404(Departement, pk=pk_department)
        birthday = request.POST.get('date')
        number = request.POST.get('number')
        message = request.POST.get('message')
        
        appointment = models.Appointment.objects.create(
            full_name=full_name,
            email_address=email_address,
            department=department,
            birthday=birthday,
            number=number,
            message=message,
        )
        data={
            'alert': self.alert,
            'success':self.success,
            }
            
            
        return render(request, self.template_name, locals())



def about(request):
    about = webmodels.About.objects.first()
    doctors = models.Doctor.objects.all()
    return render(request, "one_health/about.html", locals())


def blog_details(request):
    return render(request, "one_health/blog-details.html", locals())


def contact(request):
    return render(request, "one_health/contact.html", locals())



class PageContactView(View):
    template_name ="one_health/contact.html"
    
    def get(self, request):
        return render(request, self.template_name, locals())
    
    def post(self, request):
        name_contact = request.POST.get('name')
        email_contact = request.POST.get('adresse')
        subject_contact = request.POST.get('subject')
        message = request.POST.get('message')
        
        contact = webmodels.Contact.objects.create(
            name_contact=name_contact,
            email_contact=email_contact,
            subject_contact=subject_contact,
            message=message,
        )
        return render(request, self.template_name, locals())
    
 
def blog(request):
    return render(request, "one_health/blog.html", locals())
