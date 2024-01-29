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
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        if not isinstance(self._pages, int):
            raise TypeError('Количество страниц должно быть целым числом')
        if self._pages < 0:
            raise ValueError('Количество страниц не может быть отрицательным числом')
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> int:
        if not isinstance(self._duration, int):
            raise TypeError('Продолжительность должна быть целым числом')
        if self._duration < 0:
            raise ValueError('Продолжительность не может быть отрицательным числом')
        return self._duration

    @duration.setter
    def duration(self, new_duration: int) -> None:
        self._duration = new_duration


