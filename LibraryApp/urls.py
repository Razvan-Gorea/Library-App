from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('books/', view_all_books, name='all_books'),
    path('books/genre/<str:genre>/', view_genre, name='genre_page'),
    path('book/<str:bookname>', view_book, name='book_page'),
    path('borrower/<str:personname>', view_person, name='person_page')
]