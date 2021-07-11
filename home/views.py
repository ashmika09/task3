from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth

from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
     return render(request, 'home.html')

def register(request):
     form=UserCreationForm()
     if request.method=='POST':
          form=UserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('home')
              
          
     else:
          form=UserCreationForm()   

     context={'form':form}
     return render(request, 'register.html',context)  



def favourites(request):
     return render(request, 'favourites.html',)

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home") 

def login_request(request):
      
      if request.method=='POST':
          form=AuthenticationForm(request=request, data=request.POST)
          if form.is_valid():
               username=form.cleaned_data.get('username')
               password=form.cleaned_data.get('password')
               user=authenticate(username=username, password=password)
               if user is not None:
                    login(request,user)
                    return render(request=request, 
                    template_name='home.html',
                    context={'username':username})
               else:
                    messages.error(request,"Invalid username or password")  
                    
              
          
      else:
          messages.error(request,"Invalid username or password")  

      form=AuthenticationForm()
      return render(request=request, 
                    template_name='login.html',
                    context={'form':form})  

