from django.shortcuts import render, redirect

import bcrypt
from .models import *


def index(request):
    return render(request, 'login.html')

def login_function(request):
    if request.method == 'POST':
        # errors = User.objects.login_validator(request.POST)
        logged_user = User.objects.filter(email = request.POST['email'])
        request.session['user_id'] = logged_user[0].id

        return redirect('/dashboard')

def register(request):
    return render(request, 'register.html')

def register_function(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['conf_password']:
            new_user = User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password = request.POST['password']
            )

            request.session['user_id'] = new_user.id
            print('One')
            return redirect('/dashboard')
        else:
            print('Two')
            return redirect('/register')
    else:
        print('Three')
        return redirect('/register')

def dashboard(request):
    logged_user = User.objects.get(id = request.session['user_id'])

    context = {
        'user': logged_user
    }
    return render(request, 'dashboard.html', context)
            