from django.shortcuts import render

# Create your views here.


def page_of_book(request):
    return render(request,'book/book.html')