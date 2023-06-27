class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

        self.is_valid_date(self._day, self._month, self._year)

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        if year % 4 == 0:
            return True
        else:
            return False

    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.is_leap_year(year) is True:
            return self.DAY_OF_MONTH[1][month - 1]
        else:
            return self.DAY_OF_MONTH[0][month - 1]

    def is_valid_date(self, day: int, month: int, year: int) -> None:
        """Проверяет, является ли дата корректной"""
        if not 1 <= day <= self.get_max_day(month, year):
            raise ValueError(f"Данные не корректны!")
        else:
            print(f"Данные корректны!")

    @property
    def day(self) -> int:
        """ Возвращает количество дней."""
        return self._day

    @day.setter
    def day(self, day: int) -> None:
        """Устанавливает количество дней."""
        if not isinstance(day, int):
            raise TypeError("Количество дней должно быть типа int")
        if not 0 < day <= 31:
            raise ValueError("Количество дней должно быть положительным числом и не больше 31")
        self._day = day

    @property
    def month(self) -> int:
        """ Возвращает количество месяцев."""
        return self._month

    @month.setter
    def month(self, month: int) -> None:
        """Устанавливает количество дней."""
        if not isinstance(month, int):
            raise TypeError("Количество месяцев должно быть типа int")
        if not 1 <= month <= 12:
            raise ValueError("Количество месяцев должно быть положительным числом и не больше 12")
        self._month = month

    @property
    def year(self) -> int:
        """ Возвращает год."""
        return self._year

    @year.setter
    def year(self, year: int) -> None:
        """Устанавливает количество дней."""
        if not isinstance(year, int):
            raise TypeError("Количество лет должно быть типа int")
        if year <= 0:
            raise ValueError("Количество лет должно быть положительным числом")
        self._year = year


if __name__ == "__main__":
    d = Date(30, 12, 2001)
    # print(d.is_leap_year(2025))
    # print(d.get_max_day(8, 2023))
    print(d.month)
    d.day = 0
    print(d.day)
