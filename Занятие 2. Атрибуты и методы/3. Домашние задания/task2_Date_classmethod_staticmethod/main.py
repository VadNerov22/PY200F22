class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int):
        """Проверяет, является ли год високосным"""
        if year % 4 == 0:
            return True
        else:
            return False

    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.is_leap_year(year) is True:
            return self.DAY_OF_MONTH[1][month - 1]
        else:
            return self.DAY_OF_MONTH[0][month - 1]

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if not 1 <= day <= self.get_max_day(month, year):
            raise ValueError(f"Данные не корректны!")
        else:
            print(f"Данные корректны!")


if __name__ == "__main__":
    d = Date(31, 12, 2001)
    print(d.is_leap_year(2025))
    print(d.get_max_day(8, 2023))
