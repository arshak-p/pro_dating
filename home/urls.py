from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('personaldetails/', views.personaldetails, name='personaldetails'),
    path('jobstatus/', views.jobstatus, name='jobstatus'),
    path('jobdetails/', views.jobdetails, name='jobdetails'),
]
