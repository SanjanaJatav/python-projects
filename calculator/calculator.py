import tkinter
from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("400x650+400+100")
root.resizable(False, False)
root.configure(bg="#17161b")

equation = ""

#icon
Image_icon = PhotoImage(file = "D:/Sanjana/sanjana 02/python  projects/calculator/image/calc logo.png")
root.iconphoto(False, Image_icon)

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text = result)



label_result = Label(root,width=25,height=3,text="",font=("arial",30),fg= "#fff",bg="black")
label_result.pack()

Button(root,text="AC",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=150)
Button(root,text="%",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:show("%")).place(x=110,y=150)
Button(root,text=".",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: show(".")).place(x=210,y=150)
Button(root,text="/",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: show("/")).place(x=310,y=150)

Button(root,text="7",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2b36",command=lambda: show("7")).place(x=10,y=250)
Button(root,text="8",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2b36",command=lambda: show("8")).place(x=110,y=250)
Button(root,text="9",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2b36",command=lambda: show("9")).place(x=210,y=250)
Button(root,text="*",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: show("*")).place(x=310,y=250)

Button(root,text="4",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2b36",command=lambda: show("4")).place(x=10,y=350)
Button(root,text="5",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2b36",command=lambda: show("5")).place(x=110,y=350)
Button(root,text="6",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2b36",command=lambda: show("6")).place(x=210,y=350)
Button(root,text="-",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: show("-")).place(x=310,y=350)

Button(root,text="1",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2b36",command=lambda: show("1")).place(x=10,y=450)
Button(root,text="2",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2b36",command=lambda: show("2")).place(x=110,y=450)
Button(root,text="3",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2b36",command=lambda: show("3")).place(x=210,y=450)
Button(root,text="+",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: show("+")).place(x=310,y=450)

Button(root,text="00",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2b36",command=lambda: show("00")).place(x=10,y=550)
Button(root,text="0",width=3,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2b36",command=lambda: show("0")).place(x=110,y=550)
Button(root,text="=",width=7,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#fe9037",command=lambda: calculate()).place(x=210,y=550)


root.mainloop()