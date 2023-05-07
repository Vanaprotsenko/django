from django.shortcuts import render

# Create your views here.


def page_of_users(request):
    return render(request,'users/users.html')