books = { #словарь с названиями, авторами и годами издания книг
    1: {"title": "Зов Ктулху", "author": "Лавкрафт", "year": 1926},
    2: {"title": "Преступление и наказание", "author": "Достоевский", "year": 1865},
    3: {"title": "Мастер и Маргарита", "author": "Булгаков", "year": 1940},
    4: {"title": "1984", "author": "Оруэлл", "year": 1949},
    5: {"title": "Алые паруса", "author": "Грин", "year": 1922}
}

for book_id, book_info in books.items(): #вывод оформленного словаря
    print(f" Книга {book_id} ".center(48, '-'))
    print(f"Название: {book_info['title']}, Автор: {book_info['author']},")
    print(f"{str(book_info['year']).center(48, '-')}\n")