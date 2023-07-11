from django.shortcuts import render, redirect
from .helpers import load_books_from_file, save_books_to_file, delete_book_from_file,get_book_index_by_id,search_books_in_file
from .models import Book
from django.shortcuts import redirect, HttpResponse

def book_list(request):
    books = load_books_from_file()
    return render(request, 'library/book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        genre = request.POST['genre']
        height = request.POST['height']
        publisher = request.POST['publisher']
        books = load_books_from_file()
        book_ids = [book['book_id'] for book in books]
        book_id = max(book_ids) + 1 if book_ids else 1
        book = {
            'book_id': book_id,
            'title': title,
            'author': author,
            'genre': genre,
            'height': int(height),
            'publisher': publisher
        }
        books.append(book)
        save_books_to_file(books)
        return redirect('book_list')
    return render(request, 'library/add_book.html')


def delete_book(request, book_id):
    books = load_books_from_file()
    book_index = get_book_index_by_id(int(book_id), books)
    if book_index is not None:
        book = books[book_index]
        success = delete_book_from_file(book)
        if success:
            return redirect('book_list')
    return HttpResponse('Book not found.')


def search_books(request):
    if request.method == 'POST':
        name = request.POST['name']
        genre = request.POST['genre']
        books = search_books_in_file(name, genre)
        return render(request, 'library/book_list.html', {'books': books})
    return redirect('book_list')
