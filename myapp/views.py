from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from .models import FoodItem
from .forms import LoginForm

def login(request):  # Change the function name
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)  # Change the function name in the call
                return redirect('welcome')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def welcome(request):
    return render(request, 'welcome.html')

def menu(request):
    food_items = FoodItem.objects.all()
    return render(request, 'menu.html', {'food_items': food_items})

def logout(request):
    auth_logout(request)
    return render(request, 'logout.html')
