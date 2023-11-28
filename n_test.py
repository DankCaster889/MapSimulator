from tiles import *
from units import *

#input 1: terrain features
board = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

#assigns terrain
for i in range(5):
    for j in range(5):
        board[i][j] = Tile(i, j, "forest", "green")

#input 2: units
unit_board = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
]

#the board the battle will take place on
battle_board = [
    [0,1,0,1,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,0,1,0]
]

#unit information
b = Infantry("inf", 1, 100)

c = Infantry("inf", 1, 100)

d = Army(0, 0, "Infantry", "blue", "BLU", [b, c])

e = Army(0, 0, "Infantry", "red", "RED", [b, c])

d.place(0, 2, board[0][2])
e.place(4, 2, board[4][2])

running = True

#main loop
while running:
    for i in range(5):
        for j in range(5):
            unit_board[i][j] = 0
    
    d.place(d.x, d.y, board[d.x][d.y])
    e.place(e.x, e.y, board[e.x][e.y])

    unit_board[d.x][d.y] = d.name
    unit_board[e.x][e.y] = e.name
   
    print("============================")

    for i in range(5):
        print(unit_board[i])

    print("=THERE IS PEACE IN OUR TIME!=")
    
    e.move("down")
    d.move("up")

    if e.x == d.x and e.y == d.y:
        d.get_fighting_style()
        e.get_fighting_style()
        for i in range(5):
            for j in range(5):
                unit_board[i][j] = 0
        battle = Battle(e.x, e.y, "Ground Battle","red",[e, d])
        unit_board[e.x][e.y] = battle.type
        running = False
    
#end map output
for i in range(5):
    print(unit_board[i])
