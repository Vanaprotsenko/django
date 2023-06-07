from django.shortcuts import render,redirect

def main(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        years = request.POST.get('years')
        series = request.POST.get('series')
        speed = request.POST.get('speed')
        price = request.POST.get('price')
        type_car = request.POST.get('type')
        return redirect(f'table/{name}/{years}/{series}/{speed}/{price}/{type_car}/')
    return render(request,'app1/main.html')


def enter(request,name,years,series,speed,price,type_car):
    context = {
        'name':name,
        'type_car':type_car,
        'years':years,
        'series':series,
        'speed':speed,
        'price':price
    }
    return render(request,'app1/car_page.html',context)

