# x = 0

# for i in range(5):
#     x += 1

# print(x)

#1 Setup the game
# print (grid[0][0])
import random

grid = [[" ","1","2","3","4","5"],
        ["A","~","~","~","~","~"],
        ["B","~","~","~","~","~"],
        ["C","~","~","~","~","~"],
        ["D","~","~","~","~","~"],
        ["E","~","~","~","~","~"]]


ship_loc=["A1A2", "A1B1", "D4D5", "C4D4"]
game = random.choice(ship_loc)

shiplocation1 =game[0:2]
shiplocation2 =game[2:4]
shiphealth = 2

def print_grid():
    for row in grid:
        for column in row:
            print(column +" ", end = "")
        print("")

#2 Calculate hit or miss
print("")

for i in range(7): 

    coord = (input("what coord do you want to shoot? (A1-E5)"))

    if coord == shiplocation1:
        print("It's a hit")
        grid[1][1] = "H"
        shiphealth = shiphealth - 1
    elif coord == shiplocation2:
        print("It's a hit")
        grid[1][2] = "H"
        shiphealth = shiphealth -1
    else:
        print("You missed")
        ascii_val = ord(coord[0])-64
        print(ascii_val)
        col_val = int(coord[1])
        print(ascii_val, col_val)
        grid[ascii_val][col_val] = "M"

    print_grid()

    #3 Win check

    if shiphealth == 0:
        print ("You win")
        break

if shiphealth !=0:
    print("The ship got away")
