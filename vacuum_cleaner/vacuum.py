import random
import numpy as np
def display(room):
    print(np.matrix(room))

room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]
print("1 : Dirty Tile  0 : Clean Tile")
display(room)

x =0
y= 0
z=0
while x < 4:
    while y < 4:
        ch = random.choice([0,1])
        if ch == 1 :
            print("Vaccuming in location : ",x, y)
            room[x][y] = 0
            z+=1
        y+=1
    x+=1
    y=0
pro= (100-((z/16)*100))
display(room)
print('performance=',pro,'%')
