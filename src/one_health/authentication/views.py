from email import message
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from authentication import forms
from django.contrib.auth import login, authenticate, logout


def logout_user(request):
    logout(request)
    return redirect('home')

class RegisterPageView(View):
    template_name = 'authentication/register.html'
    form = forms.FormRegister
    
    def get(self, request):
        form = self.form()
        message =''
        return render(request, self.template_name, context={"form": form ,"message": message})

    def post(self, request):
          
        form = forms.FormRegister(request.POST)
        if form.is_valid():
            user = form.save()
            #auto-login user, login  pour connecter l’utilisateur automatiquement
            #login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        
        return render(request, 'authentication/register.html', context= {'form': form})


class loginPageView(View):
    template_name = 'authentication/login.html'
    class_form = forms.LoginForm
    message=''
    def get(self, request):
        form = self.class_form()
        message=f"Merci de bien vouloir vous connectez!"
        print(message)
        return render(request, self.template_name, context={"form": form ,"message": self.message})
    
    def post(self, request):
        form = self.class_form(request.POST)
        
        if form.is_valid():
            #recuperation des infos
            user= authenticate(request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user:
                if user.is_doctor:
                    login(request, user)
                    succes_message= f"Bienvenue{user}!"
                    return redirect('doctor')
                elif user.is_patient:
                    login(request, user)
                    message= f"Bienvenue{user}!"
                    return redirect('patient')
            
            else:
                message = f"Utilisateur Incorrect!"
        return render(request, self.template_name, context={"form": form, "message": self.message})
        

def patient(request):
    return render(request, "authentication/patient-register.html")

#@login_required
def doctor(request):
    return render(request, "authentication/doctor-register.html")

