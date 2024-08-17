from django.shortcuts import render,redirect,HttpResponse
from adminpanel.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request,'adminpanel/index.html')
    else:
        return redirect('login_page')

def reg_page(request):
    if request.method == 'POST':
        user_name = request.POST.get('user')
        email = request.POST.get('email')
        password_1 = request.POST.get('password')
        password_2 = request.POST.get('password_2')
        if password_1 != password_2:
            return redirect('reg_page')
        else:
            user_reg = User.objects.create_user(user_name,email,password_1)
            user_reg.last_name = 'Islam'
            user_reg.save()
            return redirect('login_page')
    return render(request, 'adminpanel/reg.html')

def login_page(request):
    if request.method == 'POST':
         user_name = request.POST.get('name')
         user_password = request.POST.get('password')
         user = authenticate(username = user_name, password = user_password)
         if user != None:
             login(request,user)
             return redirect('admin')
         else:
             return redirect('login_page')
    if request.user.is_authenticated:
        return redirect('admin')
    else:
        return render(request, 'adminpanel/login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')


def banner(request):
    if request.user.is_authenticated:
        return render(request,'adminpanel/banner/banner.html')
    else:
        return redirect('login_page')