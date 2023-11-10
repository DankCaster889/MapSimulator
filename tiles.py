class Tile:
    def __init__(self, x, y, type, color):
        self.x = x
        self.y = y
        self.type = type
        self.color = color

class Unit(Tile):
    def __init__(self, x, y, type, color, name, composition = None):
        super().__init__(x, y, type, color)
        self.name = name
        self.composition = composition or []

    def add_unit(self, unit):
        self.composition.append(unit)

    def combine(self, unit2):
        for i in range(len(unit2.composition)):
            self.composition.append(unit2.composition[i])

    def divide(self, factor, resulting_unit):
        new_unit = []
        for i in range((len(self.composition)/factor)):
                new_unit.append(self.composition[i])

class Battle(Tile):
    def __init__(self, x, y, type, color, units = None):
        super().__init__(x, y, type, color)
        self.units = units

class Army(Unit):
    def __init__(self, x, y, type, color, name, composition, f_style = None, location = None, troops = None):
        super().__init__(x, y, type, color, name, composition)
        self.f_style = f_style
        self.location = location
        self.troops = troops or []

    def move(self, new_x, new_y, tile):
        self.x = new_x
        self.y = new_y
        self.location = tile.type

    def get_fighting_style(self):
        if self.location == "forest":
            self.f_style = "guerilla"
        elif self.location == "mountain":
            self.f_style = "mountaineer"
        else:
            self.f_style = "generic"
