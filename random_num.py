import tkinter as tk
import random as r

choose_rand = "   Random number guessing   "
hint_text = "HINT:Enter a random number and \npress enter"
valid_int = "HINT:Enter a valid integer!!"


class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Root window attributes.
        self.title("Random number guessing")
        self.configure(bg= "black")
        self.geometry("600x400")
        self.resizable(False, False)
        
        # Widgets get defined here.
        self.intro_label = tk.Label(self,font= "arial"  ,text= choose_rand, background= "black", foreground= "blue") # Top widget

        self.hint_label = tk.Label(self,font= ("arial", 14)  ,text= hint_text, background= "black", foreground= "blue") # hint widget

        self.input_box = tk.Entry(self, font= "arial", foreground= "black" , background= "#9099a2") # Input field
        # self.input_box.insert(string="Enter a number",index=0) 

        self.guess_bt = tk.Button(self, text= "Guess", state= tk.DISABLED, bg= "#f01688",font =("arial",14),fg = "#00b7fa",command = lambda : self.guess()) # Guess button

        self.reset_bt = tk.Button(self, text= "Reset", font= ("arial", 14), bg= "#f01688", fg= "#00b7fa", command= lambda : self.reset()) # Reset button

        self.enter_bt = tk.Button(self, text= "Enter", font= ("arial", 14), bg= "#f01688", fg= "#00b7fa", command= lambda : self.enter()) # Enter button

        self.quit_bt = tk.Button(self, text= "Quit", bg= "#ff2929",font =("arial",14),fg = "#00b7fa",command = quit) # Quit button


        # Alignment if widgets
        self.intro_label.place(x= 10, y= 50)
        self.input_box.place(x= 30, y= 90)
        self.guess_bt.place(x= 30, y= 130)
        self.enter_bt.place(x= 110, y= 130)
        self.hint_label.place(x= 300, y= 40)
        self.reset_bt.place(x= 30, y= 200)
        self.quit_bt.place(x= 110, y= 200)

    def enter(self):
        """
        Get a number which will be the range for random numbers
        and generate a random number from the range.
        """
        global rand_num, range_
        
        try:
            range_ = int(self.input_box.get())
            self.input_box.delete(0,tk.END)
            rand_num = r.randint(0,range_)
            self.enter_bt.configure(state= tk.DISABLED)
            self.guess_bt.configure(state= tk.ACTIVE)
            self.hint_label.configure(text= f"HINT:Guess a number from\n0 to {range_}")
        except ValueError:
            self.input_box.delete(0,tk.END)
            self.hint_label.configure(text= valid_int)
        else:
            print(rand_num)     # Test code

    def guess(self):
        """
        Get a guess number and find it matches the random
        number or not also proovide a hint message. if 
        random number matches guess number send a congrats
        message. 
        """
        try:        
            guessed = int(self.input_box.get())

            if guessed != rand_num:
                self.input_box.delete(0,tk.END)
                left_limit = r.randint(0,rand_num-1)
                right_limit = r.randint(rand_num+1, range_)
                hint = f"HINT: the number is between \n{left_limit} and {right_limit}"
                self.hint_label.configure(text= hint)
            else:
                self.hint_label.configure(text= "CONGRATS: you guessed it right!")
        except ValueError:
            self.input_box.delete(0,tk.END)
            self.hint_label.configure(text= valid_int)


    def reset(self):
        """ Reset the entire game to intial state """
        self.input_box.delete(0,tk.END)
        self.hint_label.configure(text= hint_text)
        self.guess_bt.configure(state= tk.DISABLED)
        self.enter_bt.configure(state= tk.ACTIVE)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
