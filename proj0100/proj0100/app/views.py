from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Comp

def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        name = request.POST.get('name')
        price = request.POST.get('price')
        model = request.POST.get('model')
        year = request.POST.get('year')
        size = request.POST.get('size')
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        Comp.objects.create(name=name, model=model,price=price, year=year, size=size,image = file_url)
    comp_all = Comp.objects.all()
    context = {
        'comp_all': comp_all,
    }
    return render(request, 'app/main.html',context)





