from django.shortcuts import render
from .models import Car

# Create your views here.

def main(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        year = request.POST.get('year')
        madel = request.POST.get('madel')
        probeg = request.POST.get('probeg')
        Car.objects.create(name=name, price=price, year=year,madel=madel, probeg=probeg)
    return render(request,'app/main.html')

def info(request):
    cars = Car.objects.all()
    context ={
        'cars': cars,
    }
    return render(request,'app/info.html',context)


def info_one(request,id):
    car = Car.objects.get(id=id)
    context ={
        'car': car,
    }
    return render(request,'app/info_one.html',context)





