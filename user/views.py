from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . forms import RegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def user_main(request):
    current_user = request.user
    all_users = User.objects.all()
    return render(request, 'user.html', {'user' : current_user , 'all_users' : all_users})    

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            
            if password == confirm_password:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, 'Register berhasil')
            else:
                messages.error(request, 'Password dan konfirmasi password tidak sesuai')
                return render(request, 'register.html', {'form' : form})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form' : form})

def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.success('User Berhasil Dihapus')
    return render('user')

