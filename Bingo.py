#pip install flet 

import random
from random import randint
import tkinter

# y = []
# a = 0

# x = randint(1, 75)
# z = x in y
# y.append(x)

# print(x)
# print(y)
# print(z)

def bingo():
    while a == 0:
        y.append(x)
        x = randint(1, 75)
        z = x in y
        if z == True:
            continue
        else:
            print(x)
            if x == 75:
                print(y)
                break

#GUI
root = tkinter.Tk()

root.title(u"Software Title") #title
root.geometry("400x300") #size

Static1 = tkinter.Label(text = u"test") #label 色指定(, foreground='#ff0000', background='#ffaacc')
#Static1.place(x=150, y=228)#place
Static1.pack()

Button1 = tkinter.Button(text=u"Go!", width=10)
Button1.bind("<Button-1>", bingo)
Button2 = tkinter.Button(text=u"履歴", width=10)
Button1.pack()
Button2.pack()

root.mainloop()




#https://qiita.com/nnahito/items/ad1428a30738b3d93762