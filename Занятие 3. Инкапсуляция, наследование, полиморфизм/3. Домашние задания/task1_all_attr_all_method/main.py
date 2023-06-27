class Parent:
    atr = 12
    _par_atr = "name"
    __par_atr = 154

    def __init__(self, a: int, b: float, c: str):
        self.a = a
        self._b = b
        self.__c = c

    def saf(self):
        return self.a + self._b

    def _art(self):
        return self.__c

    def __ret(self):
        print(f"__retr")

    @classmethod
    def rty(cls):
        return cls._par_atr

    @classmethod
    def _rtyyy(cls):
        return cls.__par_atr

    @classmethod
    def __qwerty(cls):
        print(f"__qwerty")

    @staticmethod
    def sadf():
        print(f"123")

    @staticmethod
    def _sadf():
        print(f"_123")

    @staticmethod
    def __sadf():
        print(f"__123")


class Child(Parent):
    pass


if __name__ == "__main__":
    q = Child(1, 2, "7777")
    print(q.saf())
