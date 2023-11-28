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
    [0,0,0,1,0],
    [0,0,0,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
]

#unit information
b = Infantry("inf", 1, 100)

c = Infantry("inf", 1, 100)

d = Army(0, 0, "Infantry", "blue", "blu", [b, c])

e = Army(0, 0, "Infantry", "red", "red", [b, c])

d.place(2, 2, unit_board)
e.place(4, 4, unit_board)

running = True

#main loop
while running:
    
    d.place(d.x, d.y, unit_board)
    e.place(e.x, e.y, unit_board)

    print("============================")

    for i in range(5):
        print(unit_board[i])

    print("=THERE IS PEACE IN OUR TIME!=")
    
    path = e.find_path(d.x, d.y)
    e.move_along_path(path)

    if e.x == d.x and e.y == d.y:
        d.get_fighting_style()
        e.get_fighting_style()
        for i in range(5):
            for j in range(5):
                unit_board[i][j] = 0
        battle = Battle(e.x, e.y, "Ground Battle","red",[e, d])
        unit_board[e.x][e.y] = battle.type
        print(path)
        running = False
    
#end map output
for i in range(5):
    print(unit_board[i])
