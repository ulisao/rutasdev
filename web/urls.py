from django.contrib import admin
from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('instructions/', views.instructions, name='instructions'),
    path('routes/', views.routes, name='routes'),
]
