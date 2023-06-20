from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float],
                 add_water: Union[int, float] = 0, remove_water: Union[int, float] = 0):
        self.capacity_volume = None
        self.occupied_volume = None
        self.add_water = None
        self.remove_water = None
        self.init_capacity_volume(capacity_volume)
        self.init_occupied_volume(occupied_volume)
        self.add_water(add_water)
        self.remove_water(remove_water)

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
        if not isinstance(add_water, (int, float)):
            raise TypeError
        if add_water > (self.capacity_volume - self.occupied_volume):
            raise ValueError
        #self.add_water = add_water  # объем добавляемой жидкости в стакан
        self.occupied_volume += self.add_water

    def remove_water(self, remove_water):
        if not isinstance(remove_water, (int, float)):
            raise TypeError
        if remove_water > self.occupied_volume:
            raise ValueError
        #self.remove_water = remove_water  # объем удаляемой жидкости из стакана
        self.occupied_volume -= self.remove_water

if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.add_water(50))
    print(glass.remove_water(20))
