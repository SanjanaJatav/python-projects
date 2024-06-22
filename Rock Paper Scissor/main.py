from tkinter import *
from PIL import Image,ImageTk
from random import randint
from tkinter import messagebox

#main window
window = Tk()
window.title("Rock Paper Scissor")
window.geometry("700x550+400+100")
window.configure(background="#ffb7ce")

#icon
Image_icon = PhotoImage(file = "D:/sanjana/sanjana 02/python  projects/Rock Paper Scissor/image/file.png")
window.iconphoto(False, Image_icon)

#defining frames
frame1= Frame(window,width=500,height=500,bg="#ffb7ce")
frame1.pack(side=TOP, pady= 15)
frame2 = Frame(window,width=500,height=500,bg="#ffb7ce")
frame2.pack(side=BOTTOM, pady= 18)


#picture
rock_img =ImageTk.PhotoImage(Image.open("D:/Sanjana/sanjana 02/python  projects/Rock Paper Scissor/image/rock.png").resize((140,170)))
paper_img =ImageTk.PhotoImage(Image.open("D:/Sanjana/sanjana 02/python  projects/Rock Paper Scissor/image/paper.png").resize((140,170)))
scissor_img =ImageTk.PhotoImage(Image.open("D:/Sanjana/sanjana 02/python  projects/Rock Paper Scissor/image/scissor.png").resize((140,170)))
rock_img_comp =ImageTk.PhotoImage(Image.open("D:/Sanjana/sanjana 02/python  projects/Rock Paper Scissor/image/rock comp.png").resize((140,170)))
paper_img_comp =ImageTk.PhotoImage(Image.open("D:/Sanjana/sanjana 02/python  projects/Rock Paper Scissor/image/paper comp.png").resize((140,170)))
scissor_img_comp =ImageTk.PhotoImage(Image.open("D:/Sanjana/sanjana 02/python  projects/Rock Paper Scissor/image/scissor comp.png").resize((140,170)))
win_img =ImageTk.PhotoImage(Image.open("D:/Sanjana/sanjana 02/python  projects/Rock Paper Scissor/image/you win.png").resize((150,170)))
loose_img =ImageTk.PhotoImage(Image.open("D:/Sanjana/sanjana 02/python  projects/Rock Paper Scissor/image/you loose.png").resize((140,170)))
tie_img =ImageTk.PhotoImage(Image.open("D:/Sanjana/sanjana 02/python  projects/Rock Paper Scissor/image/tieGame.png").resize((140,120)))

#insert picture
user_label = Label(window, image=rock_img,bg="#ffb7ce")
user_label.place(x = 540, y = 170)
comp_label = Label(window, image=rock_img_comp,bg="#ffb7ce")
comp_label.place(x = 24, y = 170)

#scores
playerScore = Label(frame1,text=0,font=("Arial",40,"bold"),bg="#ffb7ce",fg="black")
playerScore.grid(row=2,column=2)
computerScore = Label(frame1,text=0,font=("Arial",40,"bold"),bg="#ffb7ce",fg="black")
computerScore.grid(row=2,column=0)

#indicators
scrore = Label(frame1,font=("Arial",25,"bold"),text="SCORES",bg="#ffb7ce",fg="white").grid(row=0,column=1)
user_indicator = Label(window,font=("Arial",20,"bold"),text="YOU",bg="#ffb7ce").place(x = 560, y = 100)
comp_indicator = Label(window,font=("Arial",20,"bold"),text="COMPUTER",bg="#ffb7ce").place(x = 23, y = 100)

#message
msg = Label(window, font=50, bg="#ffb7ce", fg="white")
msg.pack()

#update message
def updateMessages(x):
    msg["image"]= x

#update user score
def updateuserscore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)
#update comp score
def updatecompscore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

#check winner
def checkwin(player,computer):
    if player == computer:
        updateMessages(tie_img)
    elif player == "rock":
        if computer == "paper":
            updateMessages(loose_img)
            updatecompscore()
        else:
            updateMessages(win_img)
            updateuserscore()
    elif player == "paper":
        if computer == "scissor":
            updateMessages(loose_img)
            updatecompscore()
        else:
            updateMessages(win_img)
            updateuserscore()
    elif player == "scissor":
        if computer == "rock":
            updateMessages(loose_img)
            updatecompscore()
        else:
            updateMessages(win_img)
            updateuserscore()
    else:
        pass

#update choices
choices = ["rock", "paper", "scissor"]
def updatechoices(x):
#for computer
    compchoice = choices[randint(0,2)]
    if compchoice == "rock":
        comp_label.config(image=rock_img_comp)
    elif compchoice == "paper":
        comp_label.config(image=paper_img_comp)
    else:
        comp_label.config(image=scissor_img_comp)

#for user
    if x =="rock":
        user_label.config(image= rock_img)
    elif x =="paper":
        user_label.config(image= paper_img)
    else:
        user_label.config(image= scissor_img)

    checkwin(x,compchoice)

#exit
def Exit():
    answer = messagebox.askquestion("Exit Game", "Are you sure?")
    if (answer == "yes"):
        window.destroy()

def back():
    window.destroy()
    import start

#buttons
rock_cartoon = ImageTk.PhotoImage(Image.open("D:/Sanjana/sanjana 02/python  projects/Rock Paper Scissor/image/rock cartoon.png").resize((120,120)))
rock = Button(frame2, image = rock_cartoon,bg="#8fd3fe",activebackground="#ff3e4d",command=lambda:updatechoices("rock")).grid(row=2,column=1,pady=12)

paper_cartoon = ImageTk.PhotoImage(Image.open("D:/Sanjana/sanjana 02/python  projects/Rock Paper Scissor/image/paper cartoon.png").resize((120,120)))
paper = Button(frame2, image = paper_cartoon,bg="#8fd3fe",activebackground="#ff3e4d",command=lambda:updatechoices("paper")).grid(row=2,column=2,pady=12)

scissor_cartoon = ImageTk.PhotoImage(Image.open("D:/Sanjana/sanjana 02/python  projects/Rock Paper Scissor/image/scissor cartoon.png").resize((120,120)))
scissor = Button(frame2, image = scissor_cartoon,bg="#8fd3fe",activebackground="#ff3e4d",command=lambda:updatechoices("scissor")).grid(row=2,column=3,pady=12)


Exit_button = Button(window,text="EXIT",font="arial 20 bold",width=6,height=1,fg="yellow",bg="black",activebackground="#ff3e4d",command=Exit,)
Exit_button.place(x = 570, y= 490)

back_button = Button(window,text="BACK",font="arial 20 bold",width=6,height=1,fg="yellow",bg="black",activebackground="#ff3e4d",command=back)
back_button.place(x = 23, y= 490)

##fad02e
##ff3e4d
window.mainloop()