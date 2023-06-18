from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
# Create your views here.


def register(request):
    context ={

    }
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if first_name and last_name and username and password and confirm_password:
            if len(password) >= 8:
                if password == confirm_password:
                    try:

                        User.objects.create_user(first_name=first_name,last_name = last_name,username=username, password=password)
                    except IntegrityError:
                        context['error'] = 'Такий користувач вже існує'
        

                else:
                    context['error'] = 'Паролі не співпадають'
            else:
                context['error']="Довжина пароля повинна бути 8 або більше символів"
        else:
            context['error']="Заповнти усі поля"
    
    
    return render(request, 'user/register.html',context)    



def auth(request):
    if request.user.is_authenticated:
        return redirect('main')

    context ={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            login(request,user)
        else:
            context['error']="Логін чи пароль неправильні"

    return render(request, 'user/auth.html',context)