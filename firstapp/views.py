from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import BookForm

from .models import Book
# Create your views here.

def index(request):
    book_list=Book.objects.all()
    context ={
        'book_list':book_list
    }
    return render(request,'firstapp/index.html',context)

def detail(request,book_id):
    book=Book.objects.get(id=book_id)
    
    return render(request,'firstapp/details.html',{
        'book':book
    })

def add_book(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        book_image=request.FILES['book_image']
        book=Book(name=name, desc=desc, price=price, book_image=book_image)
        book.save()

    return render(request,'firstapp/add_book.html')

def update(request,id):
    book=Book.objects.get(id=id)
    # instance is the book that we want to edit, we receive that using the specified id
    form= BookForm(request.POST or None, request.FILES,instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'firstapp/edit.html',{'form':form,'book':book})
