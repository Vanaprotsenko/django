from django.shortcuts import render
from .models import Comp
from django.core.files.storage import FileSystemStorage

def main(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        firm = request.POST.get('firm')
        year = request.POST.get('year')
        size = request.POST.get('size')
        price = request.POST.get('price')
        media = request.POST.get('media')
        Comp.objects.create(name=name, firm=firm, year=year, size=size, price=price,media=media)
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
        'img':'image/img.jpg'
        
    }
    return render(request, 'app/filter.html', context)




def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        context = {
            'file_url': file_url
        }
        return render(request, 'app/main.html',context)
    return render(request, 'app/main.html')













