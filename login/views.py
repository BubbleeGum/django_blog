from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Berhasil')
                return redirect('dashboard')
            else:
                messages.error(request, 'Username atau password yang dimasukkan salah')
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')