from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

# Create your views here.

from .models import Book,Author
from django.views import View
from .forms import BookForm,AuthorForm


def listbook(request):

    books=Book.objects.all()

    # pagination
    paginator=Paginator(books,5)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page(page_number)

    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    #  pagination ends

    return render(request,'admin/listbook.html',{'books' : books,'page':page})

#  to display a particular data
def detailsView(request,book_id):

    book = Book.objects.get(id=book_id)
    return render(request,'admin/detailsview.html',{'book' : book})


def updateBook(request,book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES,instance=book)  # instance to recognize the correspoding model

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm(instance=book)
    return render(request,'admin/updateview.html',{'form': form})


def deleteView(request,book_id):

    book=Book.objects.get(id=book_id)

    if request.method == 'POST':

        book.delete()

        return redirect('/')


    return render(request,'admin/deleteview.html',{'book':book})


#  create book using form method
def createBook(request):

    books = Book.objects.all()

    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()

    return render(request,'admin/book.html',{'form':form,'books':books})


# create author using form method
def Create_Author(request):

    if request.method == 'POST':

        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AuthorForm()

    return render(request,'admin/author.html',{'form':form})




def index(request):
    return render(request,'admin/base.html')


def Search_Book(request):

    query=None
    books=None

    if 'q' in request.GET:

        query= request.GET.get('q')
        books= Book.objects.filter(Q(title__icontains=query)|Q(author__name__icontains=query))

    else:
        books=[]

    context={'books':books,'query':query}

    return render(request,'admin/search.html',context)


