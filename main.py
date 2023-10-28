import tkinter as tk
import numpy as np
import noise
import matplotlib.pyplot as plt

class Noise:
    def __init__(self, width, height, scale, octaves, persistence, lacunarity, seed):
        self.width = width
        self.height = height
        self.scale = scale
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        self.seed = seed
        self.map = None
        self.units = []
        self.markers = []

    def map_gen(self):
        topo_map = np.zeros((self.height, self.width))
        for i in range(self.width):
            for j in range(self.height):
                x = i / self.width - 0.5
                y = j / self.height - 0.5
                topo_map[i][j] = noise.pnoise2(x*self.scale, 
                        y*self.scale, 
                        octaves=self.octaves, 
                        persistence=self.persistence, 
                        lacunarity = self.lacunarity, 
                        repeatx=1024, 
                        repeaty=1024, 
                        base=self.seed)
        topo_map = (topo_map - np.min(topo_map)) / (np.max(topo_map) - np.min(topo_map))
        self.map = topo_map

    def add_marker(self, x, y, label):
        self.markers.append((x, y, label))

    def add_unit(self, unit):
        self.units.append(unit)

    def move_units(self, x, y):
        for unit in self.markers:
            unit.x = x
            unit.y = y

    def show(self, canvas):
        canvas.delete("all")
        for i in range(self.width):
            for j in range(self.height):
                color = f'#{int(self.map[i][j] * 255):02x}{int(self.map[i][j] * 255):02x}{int(self.map[i][j] * 255):02x}'
                canvas.create_rectangle(i, j, i+1, j+1, fill=color, outline = "")
            
            for marker in self.markers:
                x, y, label = marker
                canvas.create_text(x, y, text=label, fill="white", font=("Helvetica", 12))

            for unit in self.units:
                x, y, color = unit.x, unit.y, unit.color
                canvas.create_rectangle(x - 10, y - 5, x + 10, y + 5, fill=color, outline = "")

class Unit:
    def __init__(self, x, y, hp, color, inv=None):
        self.x = x
        self.y = y
        self.hp = hp
        self.color = color
        self.inv = inv or []

    def combine(self, unit2):
        self.hp += unit2.hp
    
    def divide(self, new_unit):
        new_unit.hp = self.hp / 2
        self.hp = self.hp / 2

b = Unit(300, 100, 4, "blue")
a = Unit(400, 200, 2, "red")

c = Noise(500, 500, 100.0, 6, 0.5, 2.0, 0)

def update_display():
    c.show(canvas)

root = tk.Tk()
root.title("Map")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

print(a.hp)
print(b.hp)
b.combine(a)
b.divide(a)
print(a.hp)
print(b.hp)
c.map_gen()
c.add_unit(a)
c.add_unit(b)
c.add_marker(250, 200, "Base")
update_display()
root.mainloop()


