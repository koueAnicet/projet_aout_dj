from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from authentication.models import User
from service.models import Departement
from web import models as webmodels
from service import models
from django.template.defaultfilters import slugify
from datetime import date
import requests
import json
import random

URLS = "https://newsapi.org/v2/everything?q=oms&from="+str(date.today())+"&sortBy=publishedAt&apiKey=bd48bd00db6d4feab29c5a6aa5582cd0"


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

        articles_response= data['articles']
        # faire un choix de 4 elements
        articles =  random.choices(articles_response, k=6)
        # print("gggggggg")
        # print('longeur:', len(articles), 'slug:', (slugify(articles[1]["title"])))
        # list_result = []
        for art in articles:
            list_result1= art['publishedAt'][:10]#caracteres
            list_result2= art['publishedAt'][11:18]#interval caractere

        #totalResult = data['totalResults']
        #articles= data['articles'][:6]
        
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


def blog_details(request, sluge_str):
    resul = requests.get(URLS)
    data = json.loads(resul.text)

    articles_response= data['articles'] 
    
    element = sluge_str
    strings = element.split("-")
    
    deslugify =""
    for i in strings:
        deslugify +=i + " "
        #break
    # if deslugify == articles_response[2]:
    #     print(deslugify)
    for el in random.choices(articles_response, k=len(articles_response)):
       
        # print(el['title'])
        # print(deslugify, "\n")
        if deslugify ==  el['title']:
            print("&&&&#####@@@@@@\n") 
            
            print(el['title'], "\n")
            print(el['urlToImage'], "\n")
            print(el['content'], "\n")
            print(el['description'], "\n")
            
           
            print(deslugify)
        continue   
   
    return render(request, "one_health/blog-details.html", locals())


def contact(request):
    return render(request, "one_health/contact.html", locals())



class PageContactView(View):
    template_name ="one_health/contact.html"
    
    def get(self, request):
        return render(request, self.template_name, locals())
    @login_required
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
    #----------API---------------#

    resul = requests.get(URLS)
    data = json.loads(resul.text)
    articles_response= data['articles']
    
    articles =  random.choices(articles_response, k=10)
    list_result = []
    for art in articles:
        list_result1= art['publishedAt'][:10]
        list_result2= art['publishedAt'][11:18]

    return render(request, "one_health/blog.html", locals())


def home_register(request):
    return render(request, "one_health/home-register.html", locals())