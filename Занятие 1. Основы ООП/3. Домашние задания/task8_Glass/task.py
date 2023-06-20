from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.occupied_volume = None
        self.init_capacity_volume(capacity_volume)
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

    def init_occupied_volume(self, occupied_volume):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume

    def add_water(self, add_water):
        # объем добавляемой жидкости в стакан
        if not isinstance(add_water, (int, float)):
            raise TypeError
        if add_water > (self.capacity_volume - self.occupied_volume):
            raise ValueError(f"Объем добавляемой жидкости д.б. меньше или равен свободному месту")
        self.occupied_volume += add_water

    def remove_water(self, remove_water):
        # объем выливаемой жидкости из стакана
        if not isinstance(remove_water, (int, float)):
            raise TypeError
        if remove_water > self.occupied_volume:
            raise ValueError(f"Объем выливаемой жидкости д.б. меньше имеющегося")
        self.occupied_volume -= remove_water

if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    glass.add_water(50)
    print(glass.occupied_volume)
    glass.remove_water(20)
    print(glass.occupied_volume)
