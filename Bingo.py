import random
from random import randint
import tkinter as tk
import csv

y = []

def bingo(event):
    global x,y,z,b
    a = 0
    while a == 0:
        x = randint(1, 75)
        z = x in y
        b = len(y)
        print("結果", b)
        if z == True:
            if b == 75:
                label2["text"] = "数字がなくなりました。"
                break
            else:
                continue
        else:
            print(x)
            label2["text"] = x
            y.append(x)
            break


def rireki(event):
    label4["text"] = y

#GUI
root = tk.Tk()

root.title(u"BINGO") #title
root.geometry("400x300") #size

label1 = tk.Label(text=u"ビンゴ",font=("Arial", 25))
label2 = tk.Label(text=u"表示先",font=("Times",16)) 
label3 = tk.Label(text=u"履歴",font=("Arial", 20))
label4 = tk.Label(text=u"表示先",font=("Times",16))
label1.pack()
label2.pack()
label3.pack()
label4.pack()

Button1 = tk.Button(text=u"Go!", width=10)
Button2 = tk.Button(text=u"履歴", width=10)
#Button3 = tk.Button(text=u"csv出力",width=10)
Button1.pack()
Button2.pack()
#Button3.pack()

Button1.bind("<Button-1>", bingo)
Button2.bind("<Button-1>", rireki)

root.mainloop()




#https://qiita.com/nnahito/items/ad1428a30738b3d93762
#https://pythonsoba.tech/tkinter/