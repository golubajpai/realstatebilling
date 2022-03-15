from django.urls import path,include
from .views import Home,get_id
from django.contrib import admin

urlpatterns = [
    path('',get_id, name="home"),
    path('admin/',get_id,name='admin'),

]