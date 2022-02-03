from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Book
# Create your views here.

def index(request):
    book_list=Book.objects.all()
    context ={
        'book_list':book_list
    }
    return render(request,'firstapp/index.html',context)

def detail(request,book_id):
    book_list=Book.objects.all()
    context ={
        'book_list':book_list
    }
    return HttpResponse("This is book % s" % book_id)