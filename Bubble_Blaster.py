from tkinter import *
HEIGHT=500
WIDTH=800
window=Tk()
window.title('Bubble Blaster')
c =Canvas(window,width=900,height=600,bg='lightblue')
c.pack()
ship_id = c.create_polygon(5,5,5,25,30,15,fill = 'red')
ship_id2 = c.create_oval(0,0,30,30,outline='darkgray')
SHIP_R = 15
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
c.move(ship_id, MID_X, MID_Y)
c.move(ship_id2, MID_X, MID_Y)
SHIP_SPD = 20
def move_ship(event):
    if event.keysym == 'Up':
        c.move(ship_id,0, -SHIP_SPD)
        c.move(ship_id2,0, -SHIP_SPD)
    elif event.keysym == 'Down':
        c.move(ship_id,0, -SHIP_SPD)
        c.move(ship_id2,0, -SHIP_SPD)
    elif event.keysym == 'Left':
        c.move(ship_id,0, -SHIP_SPD)
        c.move(ship_id2,0, -SHIP_SPD)
    elif event.keysym == 'Right':
        c.move(ship_id,0, -SHIP_SPD)
        c.move(ship_id2,0, -SHIP_SPD)
c.bind_all('<Key>', move_ship)
from random import randit
