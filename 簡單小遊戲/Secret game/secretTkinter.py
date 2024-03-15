from tkinter import *
from tkinter import messagebox
import random 


class SecretNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title('Secret Game')
        
        self.create_widgets()
         
    def create_widgets(self):
        self.min_label = Label(self.master, text="Min number")
        self.min_label.pack()
        self.min_entry = Entry(self.master)
        self.min_entry.pack()

        self.max_label = Label(self.master, text="Max number")
        self.max_label.pack()
        self.max_entry = Entry(self.master)
        self.max_entry.pack()

        self.start_button = Button(self.master, text="Start", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        try:
            self.minValue = int(self.min_entry.get())
            self.maxValue = int(self.max_entry.get())
            self.secret_number = random.randint(self.minValue, self.maxValue)
            self.master.destroy() # Closs the inital window

            self.game_window = Tk()
            self.game_window.title('Guess the Secret Number')
            self.game_window.minsize(width=200, height=80)

            self.label_range = Label(self.game_window, text=f'數字範圍{self.minValue} ~ {self.maxValue}')
            self.label_range.pack()

            self.entry_guess = Entry(self.game_window)
            self.entry_guess.pack()
            
            self.button_guess = Button(self.game_window, text='Guess', command=lambda: self.check_guess(self.secret_number))
            self.button_guess.pack()
            
            self.game_window.mainloop()
        except ValueError:
            messagebox.showerror("Error", "範圍格式輸入錯誤")
    
    def check_guess(self, secret_number):
        try:
            guess = int(self.entry_guess.get())
            if guess < self.minValue or guess > self.maxValue:
                messagebox.showinfo("Error", "輸入超出範圍")
                self.entry_guess.delete(0, 'end')
                return
            if guess == self.secret_number:
                messagebox.showinfo("Congratulations", "Boomb!\n中獎啦~")
                self.game_window.destroy()  # Close the game window
            elif guess < self.secret_number:
                self.minValue = guess
            elif guess > self.secret_number:
                self.maxValue = guess
            
            self.label_range.config(text=f"數字範圍: {self.minValue} - {self.maxValue}")
            self.entry_guess.delete(0, 'end')
        except ValueError:
            messagebox.showerror("Error", "請輸入正確數字!")


def main():
    root = Tk()
    root.minsize(width=200, height=120)
    app = SecretNumberGame(root)
    root.mainloop()

if __name__ == '__main__':
    main()