from .models import Book
def load_books_from_file():
    with open('books_list.txt', 'r') as file:
        lines = file.readlines()

    books = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 6:  # Ensure all columns are present
            book_id, title, author, genre, height, publisher = parts
            book = {
                'book_id': int(book_id),
                'title': title,
                'author': author,
                'genre': genre,
                'height': int(height),
                'publisher': publisher
            }
            books.append(book)

    return books


def save_books_to_file(books):
    with open('books_list.txt', 'w') as file:
        for book in books:
            line = f"{book['book_id']},{book['title']},{book['author']},{book['genre']},{book['height']},{book['publisher']}\n"
            file.write(line)


def get_book_index_by_id(book_id, books):
    for index, book in enumerate(books):
        if book['book_id'] == book_id:
            return index
    return None


def delete_book_from_file(book):
    books = load_books_from_file()
    book_index = get_book_index_by_id(book['book_id'], books)
    if book_index is not None:
        del books[book_index]
        save_books_to_file(books)
        return True
    else:
        return False


def search_books_in_file(name, genre):
    books = load_books_from_file()
    search_results = []
    for book in books:
        if name.lower() in book['title'].lower() and genre.lower() in book['genre'].lower():
            search_results.append(book)
    return search_results
