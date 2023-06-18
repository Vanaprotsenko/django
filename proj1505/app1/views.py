from django.shortcuts import render

def tabl(request,name,surname,old):
    
    context = {
        'name':name,
        'surname':surname,
        'old':old

    }
    return render(request, 'app1/index.html',context)

def main(request):
    return render(request,'app1/main.html')