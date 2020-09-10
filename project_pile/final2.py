from tkinter import *

name_list = []
number_list = []


    
def plus():
    global name_list
    global number_list
    
    infile = open("phone_book.dat","a")
    path_name = name2.get()
    path_num = number2.get()
    name_list.append(path_name)
    number_list.append(path_num)
    infile.close()

def first():
    global name_list
    global number_list

    name2.delete(0, END)
    number2.delete(0, END)

    name2.insert(0, str(name_list[0]))
    number2.insert(0, str(number_list[0]))

def nextda():
    global name_list
    global number_list

    irum = name2.get()
    sunsa = name_list[irum]
    daum = name_list[sunsa+1]

    irum2 = number2.get()
    sunsa2 = number_list[irum2]
    daum2 = number_list[sunsa2+1]

    name2.delete(0, END)
    number2.delete(0, END)
    name2.insert(0, daum)
    number2.insert(0, daum2)

def back():
    global name_list
    global number_list

    nameida = name2.get()
    sunsa = name_list[nameida]
    ijun = name_list[sunsa-1]

    numberda = number2.get()
    sunsa2 = number_list[numberda]
    ijun2 = number_list[sunsa2-1]

    name2.delete(0, END)
    number2.delete(0, END)
    name2.insert(0, ijun)
    number2.insert(0, ijun2)

def last():
    global name_list
    global number_list
    name2.delete(0, END)
    number2.delete(0, END)

    name2.insert(0, str(name_list[-1]))
    number2.insert(0, str(number_list[-1]))







window = Tk()

name = Label(window, text = "이름")
name2 = Entry(window)

phone_number = Label(window, text = "전화번호")
number2 = Entry(window)

app = Button(window, text = "추가", command = plus)
first = Button(window, text = "처음", command = first)
daum = Button(window, text = "다음", command = nextda)
back = Button(window, text = "이전", command = back)
last = Button(window, text = "마지막", command = last)
read = Button(window, text = "파일 읽기")

name.grid(row = 0, column = 0, columnspan = 2)
name2.grid(row = 0, column = 2, columnspan = 4)
phone_number.grid(row = 1, column = 0, columnspan = 2)
number2.grid(row = 1, column = 2, columnspan = 4)

app.grid(row = 2, column = 0)
first.grid(row = 2, column = 1)
daum.grid(row = 2, column = 2)
back.grid(row = 2, column = 3)
last.grid(row = 2, column = 4)
read.grid(row = 2, column = 5)

window.mainloop()