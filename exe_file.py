from tkinter import *

window = Tk()

window.geometry("500x500")
color = "#000000"

last_draw = None
canvas = Canvas(width=500, height=500,bg="white")
canvas.pack()

linewidth = 1
def start_drawing(event):
    global last_draw
    last_draw =event

def draw_line(event):
    global  last_draw
    if last_draw:
        canvas.create_line(last_draw.x,last_draw.y,event.x,event.y,width = linewidth,
        fill = color,capstyle=ROUND,smooth=True,splinesteps=36)
        last_draw=event

window.bind("<Button-1>",start_drawing)
window.bind("<B1-Motion>",draw_line)

window.mainloop()