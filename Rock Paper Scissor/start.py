#importing the required modules
from tkinter import *
import random
from tkinter import messagebox

#defining window
window = Tk()
window.title("Rock Paper Scissor")
window.geometry("700x550+400+100")
window.configure(background="#ffb7ce")

#icon
Image_icon = PhotoImage(file = "D:/sanjana/sanjana 02/python  projects/Rock Paper Scissor/image/file.png")
window.iconphoto(False, Image_icon)

#defining frames
frame1= Frame(window)
frame1.pack(side=TOP, pady= 14)
frame2 = Frame(window)
frame2.pack(side=BOTTOM, pady= 17)

#defining function
def start():
    window.destroy()
    import main

def Exit():
         answer = messagebox.askquestion("Exit Game", "Are you sure?")
         if(answer=="yes"):
             window.destroy()

#labeles and buttons
Label1 = Label(frame1,fg="black", text="ROCK PAPER SCISSOR",font=("Arial",40,"bold"),bg="#ffb7ce")
Label1.grid(row=2,column=2)

Image = PhotoImage(file="D:/sanjana/sanjana 02/python  projects/Rock Paper Scissor/image/file.png")
Label(window,image=Image,bg="#ffb7ce").pack()


start_button = Button(frame2,text="START",font="arial 20 bold",width=6,fg="yellow",bg="black",activebackground="#ff3e4d",command=start)
start_button.grid(row=1,column=5)

Exit_button = Button(frame2,text="EXIT",font="arial 20 bold",width=6,fg="yellow",bg="black",activebackground="#ff3e4d",command=Exit,)
Exit_button.grid(row=1,column=9)

window.mainloop()