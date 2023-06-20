BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """ Класс, описывающий объект Книга """
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализируются следующие атрибуты объекта Книга
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Возвращает строку формата, где название Книги берется с помощью атрибута name
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Возвращает валидную python строку, по которой можно инициализировать
        точно такой же экземпляр
        """
        return f"Book(id_={self.id_}, name={self.name!r}, pages={self.pages})"


class Library:
    """ Класс, описывающий объект Библиотека в которой хранятся книги """
    def __init__(self, books: list[Book] = None):
        """
        Инициализируются следующие атрибуты объекта Библиотека
        :param books: Список книг
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для добавления новой книги в библиотеку
        """
        if not self.books:
            return 1
        else:
            return self.books.__getitem__(-1).id_ + 1

    def __str__(self):
        return f"{self.books}"

    def get_index_by_book_id(self, index_: int) -> int:
        """
        Возвращает индекс книги в списке, который хранится в атрибуте экземпляра класса
        """
        for i, x in enumerate(self.books):
            if self.books.__getitem__(i).id_ == index_:
                return i
        else:
            raise ValueError(f"Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
