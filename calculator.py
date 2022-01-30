from tkinter import *

root = Tk()
root.title("Calculator")
root.configure(bg="grey")

e = Entry(root, width = 50,borderwidth= 5,fg= "white",bg = "#5b5b5b")
e.grid(padx = 10, pady = 20, column = 0, row = 0, columnspan= 4)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
      
def add():
    first = e.get()
    global f_num
    global math 
    math = "addition"
    f_num = int(first)
    e.delete(0, END)  

def sub():
    first = e.get()
    global f_num
    global math 
    math = "subtraction"
    f_num = int(first)
    e.delete(0, END)
   
def multi():
    first = e.get()
    global f_num
    global math 
    f_num = int(first)
    e.delete(0, END)
    math = "multiplication"

def div():
    first = e.get()
    global f_num
    global math 
    f_num = int(first)
    e.delete(0, END)
    math = "division"

def square():
    first = e.get()
    global f_num
    global math 
    f_num = int(first)
    e.delete(0, END)
    e.insert(0,f_num**2)

def sqroot():
    first = e.get()
    global f_num
    global math 
    f_num = int(first)
    e.delete(0, END)
    e.insert(0,f_num**0.5)

def byx():
    first=e.get()
    global f_num
    f_num=int(first)
    e.delete(0,END)
    e.insert(0,1/f_num)

def equal():
    second = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second))
    if math == "subtraction":
        e.insert(0, f_num - int(second))
    if math == "multiplication":
        e.insert(0, f_num * int(second))
    if math == "division":
        e.insert(0, f_num / int(second))
    
def button_clear():
    e.delete(0, END)

button_1 = Button(root, text ="1", padx = 40, pady = 20,bg = "black",fg="white",command=lambda: button_click(1))
button_2 = Button(root, text ="2", padx = 40, pady = 20, bg = "black",fg="white",command=lambda: button_click(2))
button_3 = Button(root, text ="3", padx = 40, pady = 20, bg = "black",fg="white",command=lambda: button_click(3))
button_4 = Button(root, text ="4", padx = 40, pady = 20,bg = "black",fg="white",command=lambda: button_click(4))
button_5 = Button(root, text ="5", padx = 40, pady = 20,bg = "black",fg="white",command=lambda: button_click(5))
button_6 = Button(root, text ="6", padx = 40, pady = 20,bg = "black",fg="white",command=lambda: button_click(6))
button_7 = Button(root, text ="7", padx = 40, pady = 20,bg = "black",fg="white",command=lambda: button_click(7))
button_8 = Button(root, text ="8", padx = 40, pady = 20,bg = "black",fg="white",command=lambda: button_click(8))
button_9 = Button(root, text ="9", padx = 40, pady = 20,bg = "black",fg="white",command=lambda: button_click(9))
button_0 = Button(root, text ="0", padx = 40, pady = 20,bg = "black",fg="white",command=lambda: button_click(0))

button_add = Button(root, text ="+", padx = 39.2, pady = 20, borderwidth = 1,command = add,bg="#5b5b5b",fg="white")
button_sub = Button(root, text ="-", padx = 41, pady = 20, borderwidth = 1,command= sub,bg="#5b5b5b",fg="white")
button_multi = Button(root, text ="*", padx = 41, pady = 20, borderwidth = 1,command = multi,bg="#5b5b5b",fg="white")
button_div = Button(root, text ="/", padx = 41, pady = 20, borderwidth = 1,command= div,bg="#5b5b5b",fg="white")
button_square = Button(root, text = "x²",padx = 38, pady = 20, borderwidth = 1,command = square,bg="#5b5b5b",fg="white")
button_sqroot = Button(root, text = "√x",padx = 36, pady = 20,bg="#5b5b5b",fg="white", borderwidth = 1,command= sqroot )
button_1byx = Button(root, text = "1/x",padx = 36, pady = 20,bg="#5b5b5b",fg="white", borderwidth = 1,command= byx )

button_clear = Button(root, text ="clear",padx = 30.5, pady = 20,command= button_clear,bg="black",fg="white")
button_equal = Button(root, text ="=", padx = 39, pady = 20, command = equal,bg="green",fg="white")
button_quit = Button(root, text="quit",padx = 32,pady=20,command = root.destroy,bg="red",fg="white",borderwidth = 1)

button_1.grid(row = 4, column = 0)
button_2.grid(row = 4, column = 1)
button_3.grid(row = 4, column = 2)

button_4.grid(row = 3, column = 0)
button_5.grid(row = 3, column = 1)
button_6.grid(row = 3, column = 2)

button_7.grid(row = 2, column = 0)
button_8.grid(row = 2, column = 1)
button_9.grid(row = 2, column = 2)
button_0.grid(row = 5, column = 1)

button_add.grid(row = 4, column = 3)
button_sub.grid(row = 3, column = 3)
button_multi.grid(row = 2, column = 3)
button_div.grid(row = 1, column = 3)

button_square.grid(row=1, column = 1)
button_sqroot.grid(row = 1, column = 2)
button_1byx.grid(row=1,column = 0)

button_clear.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 2)
button_quit.grid(row = 5,column = 3)

root.mainloop()