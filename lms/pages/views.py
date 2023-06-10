from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import BookForm , CategoryForm


def index(request):

    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()

        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()

    context = {
        'categories':Category.objects.all(),
        'books':Book.objects.all(),
        'form':BookForm(),
        'categoryform':CategoryForm(),
        'allbooks':Book.objects.filter(active=True).count(),
        'availablebooks':Book.objects.filter(status='available').count(),
        'rentalbooks':Book.objects.filter(status='rental').count(),
        'soldbooks':Book.objects.filter(status='sold').count(),
    }
    return render(request, 'pages/index.html',context)

def books(request):

    title = None
    books = Book.objects.all()

    if request.method == 'POST':
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()

    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            books = books.filter(title__icontains=title)

    context = {
        'categories':Category.objects.all(),
        'books':books,
        'categoryform':CategoryForm(),
    }
    return render(request, 'pages/books.html',context)


def updatebook(request , book_id):

    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book)
        if book_save.is_valid:
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book)
    context = {
        'form':book_save
    }
    
    return render(request, 'pages/update.html',context)


def deletebook(request, book_id):
    book = get_object_or_404(Book,id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('/')
    
    return render(request, 'pages/delete.html')
    