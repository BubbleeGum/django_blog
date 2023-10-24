from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_main, name='category'),
    path('category_create/', views.category_create, name='category_create'),
    path('delete/', views.category_delete, name='delete'),
]