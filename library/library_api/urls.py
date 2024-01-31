
from django.urls import path
from .views import *

urlpatterns = [
    path('create_user/',create_user, name='create-user'),
    
    path('list_user/',list_users, name='list-users'),
    
    path('user/<int:user_id>/',get_user_by_id, name='list-users'),
    
    path('add_book/', add_book, name = 'add-book'),
    
    path('book_list/', book_list, name = 'book-list'),
    
    path('book/<int:BookId>/', get_book_by_id, name='get-book-by-id'),
    
    path('update_book/<int:BookId>/', update_book, name='update-book'),
    
    path('borrow/<int:book_id>/', borrow_book,name='borrow-book'),
    
    path('return/<int:BookID>/', return_book, name='return-book'),
    
    path('borrowed_list/',get_all_borrowed_books, name='borrowed-books'),
]
