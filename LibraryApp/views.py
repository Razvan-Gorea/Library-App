from django.http import HttpResponse
from django.shortcuts import render

from .models import *
from django.shortcuts import get_object_or_404



def index(request):
    return render(request, 'index.html')

def view_all_books(request):
    all_books = Book.objects.all()
    return render(request, 'view_all_books.html', {'books': all_books})

def view_genre(request, genre):
    genre_page = Book.objects.filter(genre=genre)
    return render(request, 'genre.html', {'genres':genre_page})

def view_book(request, bookname):
    book_page = Book.objects.get(title=bookname)
    borrowings = Borrow.objects.filter(book=book_page)
    return render(request, 'book.html', {'book':book_page, 'borrowings':borrowings})

def view_person(request, personname):
    person_page = Customer.objects.get(Name=personname)
    borrowings = Borrow.objects.filter(customer=person_page)
    return render(request, 'person.html', {'person':person_page, 'borrowings':borrowings})