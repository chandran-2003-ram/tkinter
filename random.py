from tkinter import *
import random

root = Tk()
root.title("Random number guessing")
root.configure(bg="black")
root.geometry("600x400")
root.resizable(width = False, height=False)

ran = random.randint(0,1000)
turn = 0

def update(text):
    result.configure(text=text)

def new_game():
    global ran, turn
    guess.config(state = 'normal')
    ran = random.randint(0,1000)
    turn = 0
    update(text = "guess number between 0 and 1000")

def game():
    num = int(entry.get())

    global turn
    
    if num != ran:
        turn += 1
        result = "Wrong guess try again"
        if ran < num:
            hint = "The number lies between 0 and {}".format(num)
        else:
            hint = "The number lies between {} and 1000".format(num)
        result +="\n hint \n"+ hint
    elif ran == num:
        result = "You guessed the correct number after {} retries".format(turn)
        guess.config(state='disabled')
        result += "\n"+"click play game for new game"

    update(result)

entry = Entry(root,font = "arial",textvariable=StringVar, bg = "#9099a2",fg = "black")
entry.place(x=170, y =150)

title = Label(root, text = "Random number guessing", font =("arial",14), bg = "black",fg = "#00b7fa")
title.place(x=180, y = 50)

result = Label(root, text = "Click on play to start a new game", font = ("arial",12), bg = "black",fg = "#00b7fa")
result.place(x = 170, y = 210)

play = Button(root, text = "Play Game",bg = "#3d85c6",font =("arial",14),fg = "#ff2929",command=new_game)
play.place(x=140, y=300)

quitb = Button(root, text="Quit",bg = "#ff2929",font =("arial",14),fg = "#00b7fa",command = quit,padx = 30)
quitb.place(x = 350, y = 300)

guess = Button(root, text = "Guess", font =("arial",14), state='disabled',bg = "#f01688", command=game,fg = "#00b7fa")
guess.place(x = 420, y = 145)


root.mainloop()