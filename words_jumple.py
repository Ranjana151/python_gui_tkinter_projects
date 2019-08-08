from tkinter import *
from tkinter import messagebox
import  random
import time

words=['h v e e i c a','m t r u a a e','	c n i n t a e','	m c e x p o l','o o c d e r k','t o e y r s d','e g v n i n e','i n i f t c o',
          'o h l f i o s','o g e f i r v','r e e t p s n','e s d e d c n']
answer=['achieve','amateur','ancient','complex','crooked','destroy','evening','fiction',
        'foolish','forgive','present','descend']
global num
num = random.randrange(0,12,1)
def default():
    global answer,words,num
    lablel1.config(text=words[num])


def reset():
    global answer, words, num
    num=random.randrange(0,12,1)
    lablel1.config(text=words[num])
    entry.delete(0, END)
    lableco['text'] = ""

def check():
    global answer, words, num
    var=entry.get()
    if var==answer[num]:
        lableco.config(text="Your answer is right")


    else:
        lableco.config(text="Try Again")
        entry.delete(0,END)



root=Tk()
root.title("Jumbled Game")
root.geometry("350x400+400+300")
root.resizable(0,0)
root.config(bg="#000000")

lablel1=Label(root,text="Hello",bg="#000000",fg="white",font=("Conic sans ms",16))
lablel1.pack(pady=20,ipadx=5,ipady=5)
ans=StringVar()
entry=Entry(root,font=("Conic sans ma",16),fg="green",bg="#ffffff",width=22,relief=GROOVE,textvariable=ans,justify="center")
entry.pack(pady=5,ipadx=5,ipady=5)
Btn=Button(root,text="Check",fg="white",bg="#4b4b4b",relief=GROOVE,justify="center",width=14,font=("Conic sans ms",17),command=check)
Btn.pack(pady=40)

Btn=Button(root,text="Next",fg="white",bg="#4b4b4b",relief=GROOVE,width=14,justify="center",font=("Conic sans ms",17),command=reset)
Btn.pack(pady=20)
lableco = Label(root,  fg="black", bg="white",width=20,font=("Times",20))
lableco.pack(pady=10)
default()
root.mainloop()




