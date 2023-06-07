from django.shortcuts import render
from .models import Comp

def main(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        firm = request.POST.get('firm')
        year = request.POST.get('year')
        size = request.POST.get('size')
        price = request.POST.get('price')
        Comp.objects.create(name=name, firm=firm, year=year, size=size, price=price)
    return render(request, 'app/main.html')



def info(request):
    comps = Comp.objects.all()
    context = {
        'comps': comps,
    }
    return render(request, 'app/info.html', context)

def info_one(request,id):
    comp = Comp.objects.get(id=id)
    context = {
        'comp': comp
    }
    return render(request, 'app/info_one.html', context)


def filters(request):
    computer = Comp.objects.all()
    if request.method == 'POST':
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')

        computer = Comp.objects.filter(price__range=(min_price, max_price))
        
    
    context = {
        'computer': computer,
        
    }
    return render(request, 'app/filter.html', context)













