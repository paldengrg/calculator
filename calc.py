from tkinter import*
root=Tk()
root.title("calculator")
root.maxsize(700,1000)
root.minsize(550,700)
root.configure(bg="black")
root.iconbitmap("calc.png")

eq=""

def show(value):
    global eq
    eq+=value
    label_res.config(text=eq)


def clear():
    global eq
    eq=""
    label_res.config(text=eq)

def calc():
    global eq
    result=""
    if eq!="":
        try:
            result=eval(eq)
        except:
            result="error"
            eq=""
    label_res.config(text=result)

label_res=Label(root,width=25,height=2,text="",font=("Arial",30))
label_res.pack()



Button(root,text="C",width=3,height=1,font=("Arial Bold",30),bd=1,fg="yellow",bg="white",command=lambda:clear()).place(x=10,y=100)
Button(root,text="/",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show("/")).place(x=150,y=100)
Button(root,text="%",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show("%")).place(x=290,y=100)
Button(root,text="<--",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:clear()).place(x=430,y=100)

Button(root,text="*",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show("*")).place(x=10,y=200)
Button(root,text="7",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show("7")).place(x=150,y=200)
Button(root,text="8",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show("8")).place(x=290,y=200)
Button(root,text="9",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show("9")).place(x=430,y=200)


Button(root,text="+",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show("+")).place(x=10,y=300)
Button(root,text="4",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show("4")).place(x=150,y=300)
Button(root,text="5",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show("5")).place(x=290,y=300)
Button(root,text="6",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show("6")).place(x=430,y=300)


Button(root,text="-",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show("-")).place(x=10,y=400)
Button(root,text="1",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show("1")).place(x=150,y=400)
Button(root,text="2",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show("2")).place(x=290,y=400)
Button(root,text="3",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show("3")).place(x=430,y=400)
Button(root,text="0",width=9,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show("0")).place(x=150,y=500)
Button(root,text="=",width=3,height=1,font=("Arial Bold",30),bd=1,fg="yellow",bg="white",command=lambda:calc()).place(x=430,y=500)
Button(root,text=".",width=3,height=1,font=("Arial Bold",30),bd=1,fg="black",bg="white",command=lambda:show(".")).place(x=10,y=500)


root.mainloop()