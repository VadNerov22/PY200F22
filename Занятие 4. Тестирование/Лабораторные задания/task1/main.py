class Cars:
    """ Базовый класс автомобиля. """

    car_type = ['седан', 'лимузин', 'пикап', 'хэтчбек', 'универсал', 'лифтбек', 'минивэн',
                'купе', 'кабриолет', 'родстер', 'тарга', 'кроссовер']  # Типы кузовов лекговых автомобилей

    def __init__(self, car_brand: str = " ", engine_power: int = None, car_capacity_volume_f: int = None,
                 car_occupied_volume_f: int = None, speed: int = None):
        """
        Создаем базовый автомобиль
        :param car_brand: Марка автомобиля.
        :param engine_power: Мощность двигателя в л.с.
        :param car_capacity_volume_f: Объем топливного бака (емксоть заряда аккумуляторов электроавтомобиля).
        :param car_occupied_volume_f: Текущий объем топлива в баке (емксоть заряда аккумуляторов электроавтомобиля).
        :param speed: Скорость автомобиля в км/ч.
        """
        self._car_brand = car_brand
        self.engine_power = self.is_valid_init(engine_power)
        self._car_capacity_volume_f = car_capacity_volume_f
        self._car_occupied_volume_f = car_occupied_volume_f
        self.speed = self.is_valid_init(speed)

    @property
    def car_brand(self) -> str:
        return self._car_brand

    @property
    def car_capacity_volume_f(self) -> int:
        return self._car_capacity_volume_f

    @car_capacity_volume_f.setter
    def car_capacity_volume_f(self, value: int) -> None:
        """ Устанавливает объем топливного бака (емксоть заряда аккумуляторов для электроавто). """
        if value is not None:
            if not isinstance(value, int):
                raise TypeError("Объем топливного бака (емксоть заряда аккумуляторов) должен быть типа <int>.")
            if value <= 0:
                raise ValueError("Объем топливного бака (емксоть заряда аккумуляторов) \
                                должен быть положительном числом больше 0.")

        self._car_capacity_volume_f = value

    @property
    def car_occupied_volume_f(self) -> int:
        return self._car_occupied_volume_f

    @car_occupied_volume_f.setter
    def car_occupied_volume_f(self, value: int) -> None:
        """ Устанавливает текущий объем топлива в баке (емксоть заряда аккумуляторов для электроавто). """
        if value is not None:
            if not isinstance(value, int):
                raise TypeError("Текущий объем топлива в баке (емксоть заряда аккумуляторов) \
                                должен быть типа <int>.")
            if not 0 >= value <= self._car_capacity_volume_f:
                raise ValueError("Текущий объем топлива в баке (емксоть заряда аккумуляторов) должен быть \
                            положительном числом больше 0 и <= объму топливного бака (емкости заряда аккумуляторов).")

        self._car_occupied_volume_f = value

    @classmethod
    def is_valid_car_type(cls, type_: str) -> str:
        """ Проверяем корректность названия типа кузова автомобиля"""
        if not isinstance(type_, str):
            raise TypeError("Кузов автомобиля должен быть типа <str>.")
        if type_.lower() in cls.car_type:
            return f"'{type_.lower()}'"
        else:
            raise ValueError(f"Указан некорректный тип кузова - '{type_}'.")

    @staticmethod
    def mile_h_to_km_h(value: int) -> int:
        """ Конвертируем скорость из миль/ч в км/ч """
        return int(value * 1.609)

    def power_reserve(self, s) -> int:
        """ Определяем запас хода автомобиля
        :param s: Пройденный путь в км
        """
        return int(self._car_occupied_volume_f / ((self._car_capacity_volume_f - self._car_occupied_volume_f) / s))

    @staticmethod
    def is_valid_init(value: int) -> int:
        """ Проверяемый корректность атрибутов"""
        if value is not None:
            if not isinstance(value, int):
                raise TypeError("Значение должно быть типа <int>.")
            if value <= 0:
                raise ValueError(f"Значение должно быть > 0.")
        return value

    @staticmethod
    def to_kbt(value: int) -> int:
        """ Конвертируем л.с. в кВт """
        return int(value * 0.735)


class FuelCar(Cars):
    """ Класс автомобиля, работающиего на бензине или дизелльном топливе. """
    def __init__(self, car_brand, engine_power, car_capacity_volume_f, car_occupied_volume_f,
                 speed, type_: str = " ", engine_capacity: float = None):
        """
                Создаем автомобиль, работающий не безине (дизельном топливе)
                :param type_: Тип кузова автомобиля.
                :param engine_capacity: Объем двигателя в литрах.
                """
        super().__init__(car_brand, engine_power, car_capacity_volume_f, car_occupied_volume_f, speed)
        self.type_ = super().is_valid_car_type(type_)
        self._engine_capacity = engine_capacity

    @property
    def engine_capacity(self) -> float:
        return self._engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, value: float) -> None:
        """ Устанавливает объем двигателя. """
        if value is not None:
            if not isinstance(value, float):
                raise TypeError("Объем двигателя должен быть типа <float>.")
            if value <= 0:
                raise ValueError("Объем двигателя должен быть положительном числом больше 0.")

        self._engine_capacity = value

    def power_reserve(self, s) -> int:
        """ Определяем запас хода автомобиля, работающего на бензине (дизельном топливе)
         :param s: Пройденный путь в км
        """
        if self.speed <= 90:
            return int(super().power_reserve(s) - self._engine_capacity ** 2)
        else:
            return int(super().power_reserve(s) - (self._engine_capacity ** 3 + self.speed * 0.01))


class ElectroCar(Cars):
    """ Класс электроавтомобиля. """
    def __init__(self, car_brand, engine_power, car_capacity_volume_f, car_occupied_volume_f,
                 speed, type_: str = " "):
        """
                Создаем электроавтомобиль
                :param type_: Тип кузова автомобиля
                """
        super().__init__(car_brand, engine_power, car_capacity_volume_f, car_occupied_volume_f, speed)
        self.type_ = super().is_valid_car_type(type_)

    def power_reserve(self, s) -> int:
        """ Определяем запас хода автомобиля, работающего на бензине (дизельном топливе)
         :param s: Пройденный путь в км
        """
        if self.speed <= 110:
            return int(super().power_reserve(s) - super().to_kbt(self.engine_power) * 0.1)
        else:
            return int(super().power_reserve(s) - (super().to_kbt(self.engine_power) * 0.15 + self.speed * 0.01))


if __name__ == "__main__":
    a = Cars("Mitsubishi", 250, 100, 20, 110)
    b = ElectroCar("qwer", 150, 66, 30, 95, "кроссовер")
    c = ElectroCar("qwer2", 150, 60, 30, 120, "кроссовер")
    print(c.power_reserve(380))
