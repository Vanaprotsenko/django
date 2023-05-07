from django.shortcuts import render

# Create your views here.


def page_of_library(request):
    return render(request,'library/library.html')
