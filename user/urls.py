from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_main, name='user'),
    path('register', views.user_register, name='register'),
    path('delete/<int:int>', views.user_delete, name='delete'),
]