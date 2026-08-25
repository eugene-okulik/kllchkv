# Создаём библиотеку с книгами и школьными учебниками

class Book:
    page_material = 'бумага'
    has_text = True

    def __init__(self, title, author, pages_number, isbn, reserved=False):
        self.title = title
        self.author = author
        self.pages_number = pages_number
        self.isbn = isbn
        self.reserved = reserved


book_1 = Book(
    "Преступление и наказание",
    "Фёдор Достоевский",
    672,
    "978-5-17-090630-7"
)

book_2 = Book(
    "Мастер и Маргарита",
    "Михаил Булгаков",
    480,
    "978-5-389-01665-9"
)

book_3 = Book(
    "Война и мир",
    "Лев Толстой",
    1274,
    "978-5-17-118366-0"
)

book_4 = Book(
    "1984",
    "Джордж Оруэлл",
    320,
    "978-5-17-148844-4",
    True
)

book_5 = Book(
    "Гарри Поттер и философский камень",
    "Джоан Роулинг",
    432,
    "978-5-389-07435-4"
)

books = [book_1, book_2, book_3, book_4, book_5]
for book in books:
    text = (f"Название: {book.title}, Автор: {book.author}, "
            f"страниц: {book.pages_number}, материал: {book.page_material}")

    if book.reserved:
        print(f"{text}, зарезервирована")
    else:
        print(text)


class SchoolBook(Book):
    def __init__(self, title, author, pages_number, isbn, subject, class_id, has_tasks: bool, reserved=False):
        super().__init__(title, author, pages_number, isbn, reserved)
        self.subject = subject
        self.class_id = class_id
        self.has_tasks = has_tasks


book_al = SchoolBook(
    "Алгебра 9 класс",
    "Иван",
    1000,
    "979-5-17-090630-9",
    "Алгебра",
    "9",
    True
)

book_hi = SchoolBook(
    "История Древнего Рима",
    "Дмитрий",
    503,
    "939-5-17-090630-9",
    "История",
    "6",
    False,
    reserved=True
)

book_ru = SchoolBook(
    "Русский язык 8 класс",
    "Ольга",
    203,
    "555-5-17-090630-9",
    "Русский язык",
    "8",
    True
)

school_books = [book_al, book_hi, book_ru]
for book in school_books:
    text = (f"Название: {book.title}, Автор: {book.author}, "
            f"страниц: {book.pages_number}, предмет: {book.subject}, класс: {book.class_id}")

    if book.reserved:
        print(f"{text}, зарезервирована")
    else:
        print(text)
