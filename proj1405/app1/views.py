from django.shortcuts import render

def hello(request):
    a = 5+7
    context = {
        'number':a,
        'name':'jack',
        'title':'Me'
    }
    
    return render(request, 'app1/index.html',context)

def new(request,name):
    context = {
        'name':name
    }

    return render(request, 'app1/new.html',context)

def minus(request,number1,number2):
    context = {
        'result':number1-number2
    }
    return render(request, 'app1/cal.html',context)

def plus(request,number1,number2):
    context ={
        'result':number1+number2
    }
    return render(request, 'app1/cal.html',context)