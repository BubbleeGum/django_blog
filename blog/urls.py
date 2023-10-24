from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_main, name='blog'),
    path('blog_create', views.blog_create, name='blog_create'),
    path('blog_store', views.blog_store, name='blog_store'),
    path('blog_edit/<int:id>', views.blog_edit , name="edit"),
    # path('blog_update', views.blog_update, name='blog_update'),
]