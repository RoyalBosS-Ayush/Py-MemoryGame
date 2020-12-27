from random import shuffle
from turtle import *

tiles = list(range(8))*2
shuffle(tiles)
previous_tile,previous_index = 0,0
show = [False] * 16
tap_count = 0


def draw_board():
    "Draw white square with black outline at (x, y)."
    for x in range(-2,2):
        for y in range(-2,2):
            up()
            goto(x*50,y*50)
            down()
            for _ in range(4):
                forward(50)
                left(90)
    up()

def tile_index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 100) // 50 + ((y + 100) // 50) *4)

def tile_xy(count):
    "Convert tiles count to (x, y) coordinates."
    return ((count%4)*50-100), ((count//4)*50 - 100)

def tap(x, y):
    '''Update mark and hidden tiles based on tap.'''
    global previous_tile,previous_index,tap_count
    index = tile_index(x, y)
    x,y = tile_xy(index)

    if -100<=x<=100 and -100<=y<=100 and previous_index!=index:
        tap_count += 1

        if tiles[previous_index]==tiles[index]:
            show[index] , show[previous_index] = True,True

        draw()
        goto(x+25,y)
        color('black')
        write(tiles[index],align='center',font=('Arial',30,'normal'))

        previous_index = index
        previous_tile = tiles[index]

def draw():
    '''Draw image and tiles.'''
    clear()
    draw_board()

    for index in range(16):
        if show[index]:
            x,y = tile_xy(index)
            goto(x+25,y)
            color('black')
            write(tiles[index],align='center', font=('Arial', 30, 'normal'))

    if all(show):
        clear()
        color('Red')
        goto(0,0)
        write('You Won !!!',align='center', font=('Arial', 30, 'normal'))
        goto(0,-50)
        write(f'Moves : {tap_count}',align='center', font=('Arial', 30, 'normal'))
        done()
        exit()
        
    update()

setup(300,300, 0,0)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()