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
    
    def heuristic(self, x1, y1, x2, y2):
        return abs(x1 - x2) + (y1 - y2)

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
        self.grid = []

    def place(self, new_x, new_y, grid):
        self.x = new_x
        self.y = new_y
        self.grid = grid

    def update_location(self, grid):
        if 0 <= self.x < len(grid) and 0 <= self.y < len(self.grid[0]):
            self.location = self.grid[0][self.x][self.y]
        else:
            print("Invalid")

    def get_neighbors(self, pos):
        x, y = pos
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
                     (x - 1, y + 1), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1)]
        return [neighbor for neighbor in neighbors if 0 <= neighbor[0] < len(self.grid) and 0 <= neighbor[1] < len(self.grid[0]) and self.grid[neighbor[0]][neighbor[1]] == 0 ]

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
    
    def move_along_path(self, path):
        for position in path:
            self.x, self.y = position
            self.place(self.x, self.y, self.grid)

    def find_path(self, target_x, target_y):
        open_set = [(self.x, self.y)]
        came_from = {}
        g_score = {(self.x, self.y): 0}
        f_score = {(self.x, self.y): self.heuristic(self.x, self.y, target_x, target_y)}

        while open_set:
            current = min(open_set, key=lambda pos: f_score[pos])
            if current == (target_x, target_y):
                return self.reconstruct_path(came_from, target_x, target_y)

        open_set.remove(current)
        for neighbor in self.get_neighbors(current, self.grid):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + self.heuristic(neighbor[0], neighbor[1], target_x, target_y)
                if neighbor not in open_set:
                    open_set.append(neighbor)

        return None

    def reconstruct_path(self, came_from, target_x, target_y):
        path = [(target_x, target_y)]
        while (target_x, target_y) in came_from:
            target_x, target_y = came_from[(target_x, target_y)]
            path.append((target_x, target_y))
        return path[::-1]

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

