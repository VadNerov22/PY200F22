from typing import Union
import doctest


class BodyAnimal:
    """
    Класс описывающий тело животного
    """
    def __init__(self, weight: Union[int, float], height: Union[int, float]):
        """
        Создаем тело животного
        :param weight: Вес животного в килограммах
        :param height: Рост животного в метрах
        """
        self.weight = self.init_body(weight)
        self.height = self.init_body(height)

    def init_body(self, value) -> float:
        """
        Осуществляет проверку введенных данных: являются ли целым (вещественным) числом
        и значением больше '0' или нет
        """
        if not isinstance(value, (int, float)):
            raise TypeError(f"Значение должно быть (int, float), а не {type(value)}!")
        if value <= 0:
            raise ValueError(f"Значение должно быть больше  '0'!")
        else:
            return value

    def get_pounds_to_kg(self) -> float:
        """
        Осуществляет конвертацию из фунтов в килограммы
        """
        return self.weight * 0.453592

    def get_ft_to_km_ch(self) -> float:
        """
        Осуществляет конвертацию из футов в метры
        """
        return self.height * 0.3048

    def get_deceleration(self) -> float:
        """
        Возвращает значение понижающего коэффициента скорости животного
        """
        sub_kf = (self.weight / (self.height ** 2)) * 0.01
        return round(sub_kf, 2)


class TraitsAnimal:
    """
    Класс описывающий дополнительные признаки животного
    """
    def __init__(self, years: int, endurance: int, speed: int):
        """
        Создаем дополнительные признаки животного
        :param years: Возраст животного (полных лет)
        :param endurance: Выносливость животного от 0 до 100%
        :param speed: Максимальная скорость животного в м/с
        """
        self.years = self.init_traits(years)
        self.speed = self.init_traits(speed)
        self.endurance = self.init_endurance(endurance)

    def init_traits(self, value) -> int:
        """
        Осуществляет проверку введенных данных: являются ли целым числом
        и значением больше '0' или нет
        """
        if not isinstance(value, int):
            raise TypeError(f"Значение должно быть 'int', а не {type(value)}!")
        if value < 0:
            raise ValueError(f"Значение должно быть больше  '0'!")
        else:
            return value

    def init_endurance(self, value) -> float:
        """
        Осуществляет проверку введенных данных выносливости животного: является ли целым числом
        и значением в пределах от 0 до 100
            """
        if not isinstance(value, int):
            raise TypeError(f"Значение должно быть int, а не {type(value)}!")
        if value < 0 or value > 100:
            raise ValueError(f"Значение должно быть в пределах  от 0 до 100")
        else:
            return (100 - value) / 10

    def get_deceleration(self) -> float:
        """
        Возвращает значение понижающего коэффициента скорости животного
        """
        if self.years <= 5:
            sub_kf = self.endurance
        else:
            sub_kf = self.endurance + (self.years / 20)
        return round(sub_kf, 2)


class SkinAnimal:
    """
    Класс описывающий шкуру животного
    """
    def __init__(self, color: str, skin_moisture: int):
        """
        Создаем шкуру животного
        :param color: Цвет шкуры животного
        :param skin_moisture: Вложность шкуры животного от 0 до 100%
        """
        self.color = self.init_color(color)
        self.skin_moisture = self.init_moisture(skin_moisture)

    def init_color(self, color):
        if not isinstance(color, str):
            raise TypeError(f"Цвет животного должен быть 'str', а не {type(color)}")
        return color

    def init_moisture(self, value) -> float:
        """
        Осуществляет проверку введенных данных вложности шкуры животного: является ли целым числом
        и значением в пределах от 0 до 100
            """
        if not isinstance(value, int):
            raise TypeError(f"Значение должно быть int, а не {type(value)}!")
        if value < 0 or value > 100:
            raise ValueError(f"Значение должно быть в пределах  от 0 до 100")
        else:
            return value

    def get_deceleration(self) -> float:
        """
        Возвращает значение понижающего коэффициента скорости животного
        """
        sub_kf = self.skin_moisture / 100
        return round(sub_kf, 2)


class Animal:
    """
    Класс описывающий животного
    """
    def __init__(self,  body: BodyAnimal, skin: SkinAnimal, traits: TraitsAnimal):
        """
        Создаем животного
        """
        self.body = body
        self.skin = skin
        self.traits = traits

    def get_speed(self) -> float:
        """
        Возвращает скорость бега животного с учетом его параметров
        """
        sub_kf = 0
        for obj in [self.body, self.skin, self.traits]:
            sub_kf += obj.get_deceleration()
        return self.traits.speed - sub_kf

    def __str__(self) ->str:
        """
        Представление данных о беге животного
        """
        return (f"Животное цвет шкуры {self.skin.color} бежит со скоростью {self.get_speed()} м/с")


if __name__ == "__main__":
    doctest.testmod()
    # body = BodyAnimal(2.5, 1.2)
    # skin = SkinAnimal("желтый", 21)
    # traits = TraitsAnimal(3, 88, 31)
    # gepard = Animal(body, skin, traits)
    # print(gepard)