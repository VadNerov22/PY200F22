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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
