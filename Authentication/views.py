from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, ' user login successfully!  ')
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Username and password are required.")
    
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,"you have been logged out")
    return redirect('login')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists. Choose a different username.'})

        if password != confirm_password:
            return render(request, 'Register.html', {'error': 'Passwords do not match.'})

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        
        # Redirect to the login page after successful registration
        messages.success(request, ' user Register  successfully!  ')
        return redirect('login')

    return render(request, 'register.html')

