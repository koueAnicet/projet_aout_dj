"""one_health URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


from web import views
import authentication.views as authentication_view
import service.views as service_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PageHomeView.as_view(), name="home"),
    path('blog/', views.blog, name="blog"),
    path('about/', views.about, name="about"),
    path('blog-details/', views.blog_details, name="blog_details"),
    path('contact/', views.PageContactView.as_view(), name="contact"),
    #path('doctors/', views.doctors, name="doctors"),
    path('doctors/', views.PageDoctorView.as_view(), name="doctors"),
    path('register/', authentication_view.RegisterPageView.as_view(), name="register"),
    path('login/', authentication_view.loginPageView.as_view(), name="login"),
    path('doct/', authentication_view.register_doctor, name="doct"),
    path('pat/', authentication_view.register_patient, name="pat"),
    path('logout/', authentication_view.logout_user, name="logout"),
    path('tinymce/', include('tinymce.urls')),
   
]
if  settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )