class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга '{self.name}'. Автор '{self.author}'."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс бумажной книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        """ Устанавливает количество страниц в книге. """
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть типа 'int'.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self._pages = value

    def __str__(self):
        return f"Книга '{self.name}'. Автор '{self.author}'. Страниц - {self.pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """ Класс аудиокниги. """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        """ Устанавливает продолжительность аудиокниги. """
        if not isinstance(value, float):
            raise TypeError("Продолжительность аудиокниги должна быть типа 'float'.")
        if value <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительным числом.")
        self._duration = value

    def __str__(self):
        return f"Книга '{self.name}'. Автор '{self.author}'. Продолжительность - {self.duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"
