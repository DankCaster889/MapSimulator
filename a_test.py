from tiles import *
from units import *
import numpy as np

unit_board = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

for i in range(5):
    for j in range(5):
        unit_board[i][j] = Tile(i, j, "forest", "green")

#the board the battle will take place on
battle_board = [
    [0,1,0,1,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,0,1,0]
]

board = np.vstack((unit_board, battle_board))
#unit information
b = Infantry("inf", 1, 100)

c = Infantry("inf", 1, 100)

d = Army(0, 0, "Infantry", "blue", "BLU", [b, c])

e = Army(0, 0, "Infantry", "red", "RED", [b, c])

d.place(0, 2, unit_board)
e.place(4, 2, unit_board)

e.find_path(d.x, d.y)
