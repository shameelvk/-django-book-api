from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializer import BookSerializer

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data=request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):

    if request.method == 'GET':
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data,partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response("deleted recode")

