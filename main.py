import turtle as trtl
import random as rand
import sys
# NOTE: if you press keybinds to fast the system will crash
# NOTE: the longer you play, the more delayed the keybind is 

# ---- turtles ----
grid_pen = trtl.Turtle()
wn = trtl.Screen()

# ---- configurations -----
wn.title("2048 - Colin Esperanza Edition")
wn.bgcolor("grey")
wn.setup(width=600, height=600)

# grid list abstractions

grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
    ]


grid_merged = [
[False, False, False, False],
[False, False, False, False],
[False, False, False, False],
[False, False, False, False]
]

# --- functions----

def start_screen():
    grid_pen.hideturtle()
    grid_pen.penup()
    grid_pen.shape("square")
    grid_pen.color("gold")
    grid_pen.goto(0, 75)
    grid_pen.turtlesize(stretch_wid = 5, stretch_len = 5, outline = 2)
    grid_pen.stamp()

    grid_pen.goto(0, 55)
    grid_pen.color("white")
    grid_pen.write("2048", align="center", font=("Arial", 30, "bold"))

    grid_pen.color("lightgray")
    grid_pen.sety(grid_pen.ycor() - 100)
    grid_pen.write("Press space to start!", align="center", font=("Arial", 30, "bold"))

def re_start():
    grid_pen.reset()
    wn.bgcolor("gray")

    # reset grid 

    grid[0] = [0, 0, 0, 0, 0]

    grid[1] = [0, 0, 0, 0, 0]

    grid[2] = [0, 0, 0, 0, 0]

    grid[3] = [0, 0, 0, 0, 0]

    grid[0][1] = rand.choice([2,4])
    grid[2][3] = rand.choice([2,4])

    rand.shuffle(grid)
    create_grid()

# 4 x 4 Design Grid  
def create_grid():
    # grid pen configs 
    grid_pen.penup()
    grid_pen.color("lightgray")
    grid_pen.shape("square")
    grid_pen.shapesize(7)

    colors = {
        0: "white",
        2: "linen",
        4: "moccasin",
        8: "light salmon",
        16: "tomato",
        32: "red",
        64: "orangered",
        128: "yellowgreen",
        256: "lightcoral",
        512: "steelblue",
        1024: "mediumvioletred",
        2048: "gold"
    }

    wn.tracer(False)
    
    sety = 375
    col = 0
    for rows in grid:
        row = 0
        setx = -375
        sety -= 150
        for column in rows:
            setx += 150
            grid_pen.goto(setx, sety)

            value = grid[col][row]
            color = colors[value]

            grid_pen.color(color)
            grid_pen.stamp()
            grid_pen.color("dimgray")
            
            if column != 2 and column != 4:
                grid_pen.color("white")

            if column == 0:
                number = ""

            elif column == 2:
                grid_pen.sety(grid_pen.ycor() - 50)
                grid_pen.write("2", align="center", font=("Arial", 65, "bold"))
                
            elif column == 4:
                grid_pen.sety(grid_pen.ycor() - 50)
                grid_pen.write("4", align="center", font=("Arial", 65, "bold"))
                
            elif column == 8:
                grid_pen.sety(grid_pen.ycor() - 50)
                grid_pen.write("8", align="center", font=("Arial", 65, "bold"))
                
            elif column == 16:
                grid_pen.sety(grid_pen.ycor() - 50)
                grid_pen.write("16", align="center", font=("Arial", 65, "bold"))
                
            elif column == 32:
                grid_pen.sety(grid_pen.ycor() - 50)
                grid_pen.write("32", align="center", font=("Arial", 65, "bold"))
                
            elif column == 64:
                grid_pen.sety(grid_pen.ycor() - 50)
                grid_pen.write("64", align="center", font=("Arial", 65, "bold"))
                
            elif column == 128:
                grid_pen.sety(grid_pen.ycor() - 45)
                grid_pen.write("128", align="center", font=("Arial", 60, "bold"))
                
            elif column == 256:
                grid_pen.sety(grid_pen.ycor() - 45)
                grid_pen.write("256", align="center", font=("Arial", 60, "bold"))
                
            elif column == 512:
                grid_pen.sety(grid_pen.ycor() - 45)
                grid_pen.write("512", align="center", font=("Arial", 60, "bold"))
                
            elif column == 1024:
                grid_pen.sety(grid_pen.ycor() - 30)
                grid_pen.write("1024", align="center", font=("Arial", 40, "bold"))
            
            # cue win screen
            elif column == 2048:
                
                grid[3][3] = 2048
                
                wn.bgcolor("gold")
                grid_pen.reset()
                grid_pen.hideturtle()
                grid_pen.penup()
                grid_pen.color("dimgray")
                grid_pen.sety(grid_pen.ycor() + 80)


                # Win Screen
                grid_pen.write("You Win!", align="center", font=("Arial", 75, "bold"))
                grid_pen.color("white")
                grid_pen.sety(grid_pen.ycor() - 210)
                grid_pen.write("2048", align="center", font=("Arial", 60, "bold"))


                grid_pen.sety(grid_pen.ycor() + 150)
                grid_pen.write("Press 'q' to Exit", align="center", font=("Arial", 30, "italic"))

                grid_pen.sety(grid_pen.ycor() - 60)
                grid_pen.write("Press space to try again", align="center", font=("Arial", 30, "italic"))
                               
                wn.onkeypress(quit, "q")
                wn.onkeypress(re_start,"space")

                break 
                
            # cue lose screen
            if is_grid_full(grid) and column != 2048:

                wn.bgcolor("gray")
                grid_pen.reset()
                grid_pen.hideturtle()
                grid_pen.penup()
                grid_pen.color("white")
                
                grid_pen.goto(0,70)
                grid_pen.write("Game Over!", align="center", font=("Arial", 40, "bold"))

                grid_pen.goto(-70,70)
                grid_pen.setx(grid_pen.xcor() + 65)
                grid_pen.color("lightgray")
                grid_pen.sety(grid_pen.ycor() - 60)
                grid_pen.write("Press 'q' to Quit", align="center", font=("Arial", 30, "italic"))
                grid_pen.sety(grid_pen.ycor() - 60)
                grid_pen.write("Press space to try again", align="center", font=("Arial", 30, "italic"))

                wn.onkeypress(quit, "q")
                wn.onkeypress(re_start,"space")

            row += 1
        col += 1
    grid_pen.hideturtle()
    wn.update()

def quit():
    sys.exit()

# each move (up, down, right, left) adds a new value to an empty cell in the grid 
def add_random():
    full = False
    while not full:
        # grid randomly chooses an element from both row and col
        row = rand.randint(0, 3)
        col = rand.randint(0, 3)

        # then it chooses random 2 or 4 value
        value = rand.choice([2,4]) 

        # if cell is empty
        if grid[col][row] == 0:
            # empty cell becomes 2 or 4
            grid[col][row] = value
            full = True
            continue


# Is grid full? 
def is_grid_full(grid):
# Check for empty cells
# if 0 is in grid, return False
    for row in grid:
        if 0 in row:
            # Grid is not full 
            return False

# Check for adjacent cells using current_value. If same value, return False
    for col in range(len(grid)):
        for row in range(len(grid[0])):
            current_value = grid[col][row] 

            # Check right adjacent. Row + 1
            if row < len(grid[0]) - 1 and current_value == grid[col][row + 1]:
                return False # Grid is not full
            
            # Check left adjacent. Row - 1
            if row > 0 and current_value == grid[col][row - 1]:
                return False # Grid is not full

            # Check up adjacent. Col - 1
            if col > 0 and current_value == grid[col - 1][row]:
                return False # Grid is not full
            
            # Check bottom adjacent. Col + 1
            if col < len(grid[0]) - 1 and current_value == grid[col + 1][row]:
                return False # Grid is not full
            
    # return True if grid is full and no same-value adjacent cells
    return True

# Keybinds
def up():
    # Go through row by row
    for index in range(4):
        for row in range(0, 4):
            for col in range(1,4):
                # if adjacent cell is empty (no value), cell moves up & takes places of empty cell
                if grid[col-1][row] == 0:
                    grid[col-1][row] = grid[col][row]
                    grid[col][row] = 0

                    continue
            
                # if adjacent cells have the same value and values are NOT merged
                if grid[col-1][row] == grid[col][row] and not grid_merged[col-1][row]:
                    grid[col-1][row] = grid[col][row] * 2
                    grid_merged[col-1][row] = True
                    grid[col][row] = 0

                    continue

    reset_grid_merged()
    add_random()
    create_grid()


def down():
    # Go through row by row
    for index in range(4):
        for col in range(2, -1, -1):
            for row in range(0, 4):
                # if adjacent cell is empty (no value), cell moves down & takes places of empty cell
                if grid[col+1][row] == 0:
                    grid[col+1][row] = grid[col][row]
                    grid[col][row] = 0
                    row -= 1

                    continue
            
                # if adjacent cells have the same value and values are NOT merged
                if grid[col+1][row] == grid[col][row] and not grid_merged[col+1][row]:
                    grid[col+1][row] = grid[col][row] * 2
                    grid_merged[col+1][row] = True
                    grid[col][row] = 0

                    continue
                    
    reset_grid_merged()
    add_random()
    create_grid()

def right():
    # Go through row by row
    for indexes in range(4): 
        for col in range(0,4):
           for row in range(0,3):
                # if adjacent cell is empty (no value), cell moves right & takes places of empty cell
                if grid[col][row+1] == 0:
                    grid[col][row+1] = grid[col][row]
                    grid[col][row] = 0

                    row += 1

                    continue
            
                # if adjacent cells have the same value and values are NOT merged
                if grid[col][row+1] == grid[col][row] and not grid_merged[col][row+1]:
                    grid[col][row+1] = grid[col][row] * 2
                    grid_merged[col][row-1] = True
                    grid[col][row] = 0

                    continue

    reset_grid_merged()
    add_random()
    create_grid()


def left():
    # Go through row by row
    for indexes in range(4): 
        for col in range(0, 4):
            for row in range(1, 4):
                # if adjacent cell is empty (no value), cell moves left & takes places of empty cell
                if grid[col][row-1] == 0:
                    grid[col][row-1] = grid[col][row]
                    grid[col][row] = 0

                    continue
            
                # if adjacent cells have the same value and values are NOT merged
                if grid[col][row-1] == grid[col][row] and not grid_merged[col][row-1]:
                    grid[col][row-1] = grid[col][row] * 2
                    grid_merged[col][row-1] = True
                    grid[col][row] = 0

                    continue

    reset_grid_merged()
    add_random()
    create_grid()


def reset_grid_merged():
    global grid_merged
    grid_merged = [
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False]
    ] 


# --- events -----
start_screen()

wn.onkeypress(re_start, "space")
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

wn.listen()
wn.mainloop()