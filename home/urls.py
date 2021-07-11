from django.contrib import admin
from . import views
from django.urls import path

urlpatterns=[
    path("",views.index,name='home'),
    path("register/",views.register,name='register'),
    path("favourites/",views.favourites, name='favourites'),
    path("logout", views.logout_request, name="logout"),
    path("login/",views.login_request,name='login'),
]