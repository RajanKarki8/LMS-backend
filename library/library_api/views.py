from rest_framework.decorators import api_view
from .models import User, Book, BookDetails, BorrowedBooks
from .serializers import (UserSerializer, 
                BookSerializer, 
                BookDetailsSerializer, 
                BorrowedBooksSerializer)

from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone

@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def list_users(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_by_id(request, user_id):
    user = get_object_or_404(User, user_id = user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def add_book(request):
    if request.method == "POST":
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['GET'])
def book_list(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_book_by_id(request, BookId):
    book = get_object_or_404(Book, BookId = BookId)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['POST'])
def update_book(request, BookId):
    if request.method == 'POST':
        books = Book.objects.get(BookId = BookId)
        serializer = BookSerializer(instance=books, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def borrow_book(request, book_id):
    if request.method == 'POST':
        
        book = get_object_or_404(BorrowedBooks, book_id=book_id)
    # data = {'book': book.id, 'user': request.user.id}
        serializer = BorrowedBooksSerializer(book, data=request.data)    
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def return_book(request, book_id):
    borrowed_book = get_object_or_404(BorrowedBooks, book_id=book_id, user_id=request.user.id)
    borrowed_book.returned_date = timezone.now()
    borrowed_book.save()
    return Response({'message': 'Book returned successfully.'})

@api_view(['GET'])
def get_all_borrowed_books(request):
    borrowed = BorrowedBooks.objects.all()
    serializer = BorrowedBooksSerializer(borrowed, many=True)
    return Response(serializer.data)
    
