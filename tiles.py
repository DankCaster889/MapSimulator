#generic tile
class Tile:
    def __init__(self, x, y, type, color):
        self.x = x
        self.y = y
        self.type = type
        self.color = color

#generic obstacle tile
class Obstacle(Tile):
    def __init__(self, x, y, type, color, hardness):
        super().__init__(x, y, type, color)
        self.hardness = hardness

#generic unit type
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

#represents a gathering of soldiers
class Army(Unit):
    def __init__(self, x, y, type, color, name, composition, f_style = None, location = None):
        super().__init__(x, y, type, color, name, composition)
        self.f_style = f_style
        self.location = location

    def place(self, new_x, new_y, tile):
        self.x = new_x
        self.y = new_y
        self.location = tile.type
    
    def move(self, direction):
        if direction == "up":
            self.x += 1
        elif direction == "down":
            self.x -= 1
        elif direction == "left":
            self.y -= 1
        elif direction == "right":
            self.y += 1
        else:
            print("Incorrect input")

    def linear_move(self, direction, distance):
        for i in range(distance):
            if direction == "up":
                self.x += 1
            elif direction == "down":
                self.x -= 1
            elif direction == "left":
                self.y -= 1
            elif direction == "right":
                self.y += 1
            else:
                print("Incorrect input")

    def diagonal_move(self, direction, distance):
        for i in range(distance):
            if direction == "up_left":
                self.x -= 1
                self.y += 1
            elif direction == "up_right":
                self.x += 1
                self.y += 1
            elif direction == "down_left":
                self.x -= 1
                self.y -= 1
            elif direction == "down_right":
                self.x += 1
                self.y -= 1
            else:
                print("Incorrect input")

    def get_fighting_style(self):
        if self.location == "forest":
            self.f_style = "guerilla"
        elif self.location == "mountain":
            self.f_style = "mountaineer"
        else:
            self.f_style = "generic"

#battle tile to display on map
class Battle(Tile):
    def __init__(self, x, y, type, color, units = []):
        super().__init__(x, y, type, color)
        self.units = units
        self.battle()

    def battle(self):
        print("*WAR WERE DECLARED!*")
        print(f"{self.units[0].f_style} is {self.units[0].name}'s strategy")
        print(f"{self.units[1].f_style} is {self.units[1].name}'s strategy")
        print(f"{self.units[0].composition[0].name} has been hit for 5 points")
        self.units[0].composition[0].hp - 5
        print(f"{self.units[1].composition[0].name} has been hit for 5 points")
        self.units[1].composition[0].hp - 5

