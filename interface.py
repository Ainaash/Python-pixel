from tkinter import *

window =Tk()

window.title("Названи окна")
window.geometry("500x500")
window.resizable(width=False, height=False)

frame=Frame(window, bg="lightblue")
frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

label=Label(frame, text="Текст", font=100)
label.place(x=1,y=1,width=488,height=100)

def click_button1():
    label.config(text="Кнопка 1")

def click_button2():
    label.config(text="Кнопка 2")

button1=Button(frame,text="Кнопка 1",font=50, command=click_button1)
button1.place(x=200, y=200, width=100, height=50)

button2=Button(frame,text="Кнопка 2",font=50, command=click_button2)
button2.place(x=200, y=300, width=100, height=50)

window.mainloop()

