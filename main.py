import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import noise
import random
from tiles import *
from units import *

#dictionary of terrain and colors
terrain_types = {'forest':'green',
                 'desert':'yellow', 
                 'mountain':'gray',
                 'ocean':'blue'}

#Noise which generates the base map
class Noise:
    def __init__(self, width, height, canvas_width, canvas_height, tile_size, scale, octaves, persistence, lacunarity, seed):
        self.width = width
        self.height = height
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.tile_size = tile_size
        self.scale = scale
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity
        self.seed = seed
        self.map = None
        self.markers = []
        self.units = [[None for _ in range(width)] for _ in range(height)]
        self.tiles = [[None for _ in range(width)] for _ in range(height)]

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
    
    def create_tile_map(self):
        tile_width = self.canvas_width // self.width
        tile_height = self.canvas_height // self.height

        for i in range(self.width):
            for j in range(self.height):
                value = self.map[i][j]
                if value > 0.6:
                    type = "mountain"
                elif value < 0.6 and value > 0.4:
                    type = "forest"
                else:
                    type = "ocean"
                #right here is where we directly create the tile and place it in the grid
                self.tiles[i][j] = Tile(i*tile_width, j*tile_height, type, terrain_types[type])
                self.tiles[200][200] = Unit(200*tile_width, 200*tile_height, type, "red", "Infantry", [])

    def add_marker(self, x, y, label):
        self.markers.append((x, y, label))

    def add_unit(self, unit):
        self.units[unit.x][unit.y] = Unit(unit.x, unit.y, unit.type, unit.color, unit.name)

    def move_units(self, x, y):
        for unit in self.markers:
            unit.x = x
            unit.y = y

    #this is what displays the tile map onto the screen
    def show(self, canvas, zoom_x, zoom_y):
        canvas.delete("all")
        for i in range(self.width):
            for j in range(self.height):
                tile = self.tiles[i][j]
                x = tile.x * self.tile_size
                y = tile.y * self.tile_size
                canvas.create_rectangle(x, y, x + self.tile_size, y + self.tile_size, fill=tile.color, outline = "")

            for marker in self.markers:
                x, y, label = marker
                canvas.create_text(x, y, text=label, fill="white", font=("Helvetica", 12))

canvas_width = 800
canvas_height = 800
tile_size = 3

a = Unit(400, 200, "Battalion", "red", "First Regiment")
b = Infantry("Infantry", 1, 100)
a.add_unit(b)

c = Noise(800, 800, canvas_width, canvas_height, tile_size, 100.0, 6, 0.5, 2.0, 0)

c.add_unit(a)

def update_display():
    c.show(canvas, 800, 800)

root = tk.Tk()
root.title("Map")

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

c.map_gen()
c.create_tile_map()
update_display()
root.mainloop()
