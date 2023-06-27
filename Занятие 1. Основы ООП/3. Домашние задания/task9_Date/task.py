class Date:
    def __init__(self, day: int, month: int, yaer: int):
        self.day = self.init_date(day)
        self.month = self.init_date(month)
        self.yaer = self.init_date(yaer)

    def init_date(self, val):
        if not isinstance(val, int):
            raise TypeError
        return val

    def __str__(self):
        """
        Возвращает строку формата DD/MM/YYYY, где DD - день, MM - месяц, YYYY - год.
        """
        return f"{self.day:0>2}/{self.month:0>2}/{self.yaer}"

    def __repr__(self):
        """
        Возвращает валидную python строку, по которой можно инициализировать
        точно такой же экземпляр
        """
        return f"(day={self.day}, month={self.month}, yaer={self.yaer})"


if __name__ == '__main__':
    d = Date(15, 3, 2023)
    print(d)