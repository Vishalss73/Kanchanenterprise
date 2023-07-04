
from django.contrib import admin
from django.urls import path, include
from enterpriseapp import views
from .views import *

urlpatterns = [
    path('', views.Homepage, name='home'),
    path('contact', views.Contact_view, name='contact'),
    path('farmer-certificate-details', views.Farm, name='farmer-certificate-details'),
    path('about', views.About, name='about'),
    path('service', views.Service, name='service'),
    path('attractive-location', views.Attractive, name='attractive-location'),
     path('projects', views.Projects, name='projects'),
    path('project/<str:slug>', views.Project_details, name='project-details'),
    path('service/<str:slug>', views.Service_details, name='service-details'),
    path('recent-projects', views.Recentproject, name='recent-projects'),
    path('search/',views.Search,name="search"),
    path('<str:slug>', views.Single, name='single'),

]
