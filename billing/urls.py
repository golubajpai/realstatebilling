from django.urls import path,include
from .views import Home
from django.contrib import admin

urlpatterns = [
    path('',Home.as_view(), name="home"),
    path('admin/', admin.site.urls,name='admin'),

]