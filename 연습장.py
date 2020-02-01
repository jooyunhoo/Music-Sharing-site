from tkinter import *

import random

a = random.randint(1,100)

window = Tk()

def num():
    b = int(e1.get())
    if a>b:
        print("작아요")
    elif a<b:
        print("커요")
    else:
        print("정답")
    

l1 = Label(window,text=)
l1.grid(row=0,column=0)

e1 = Entry(window)
e1.grid(row=1)

b1=Button(window,text="숫자를 입력",command=num)
b1=Button(window,text="게임을 다시 실행",)

window.mainloop()
            
