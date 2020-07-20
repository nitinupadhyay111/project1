from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='classifier-index'),
    path('records/', views.firstfewfecords, name='firstfewfecords'),
    path('userlogin/', views.insertData, name='userlogin')
]
