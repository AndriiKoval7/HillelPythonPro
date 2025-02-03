"""
Створи JSON-файл з інформацією про книги, кожна книга повинна мати:
Назву
Автора
Рік видання
Наявність (True або False)
Напиши програму, яка:
Завантажує JSON-файл.
Виводить список доступних книг (наявність True).
Додає нову книгу в цей файл.
"""
import json
import os


BOOKS_FILE = 'books.json'

def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def show_books():
    books = load_books()
    if not books:
        print(f'No books found')
        return
    print(f'\nBooks found: {len(books)}')
    for ind, book in enumerate(books):
        status = "in stock" if book["in stock"] else "not in stock"
        print(f'{ind + 1}) {book["book_name"]}, author: {book["author"]}, {status}')

def save_book(book):
    with open(BOOKS_FILE, 'w', encoding='utf-8') as file:
        json.dump(book, file, ensure_ascii=False, indent=4)

def add_book(book_name, author, year, in_stock):
    books = load_books()
    books.append({
        "book_name": book_name,
        "author": author,
        "year": year,
        "in stock": in_stock
    })
    save_book(books)
    print(f'Books added: {book_name}')


show_books()
add_book('book_n','author_n',2017,True)
show_books()
