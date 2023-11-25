import tkinter as tk
import math


class Calculator_App():
    def __init__(self, w):
        #δημιουργία γραφικών παραθύρου εφαρμογής
        self.w = w
        self.w.geometry("400x500")
        self.w.title("SCIENTIFIC CALCULATOR")
        self.w.resizable(height=False, width=False)
        self.w.configure(bg='#3b3a3a')
        self.create_buttons_grid()
        self.create_entry_box()
        

    def create_buttons_grid(self):
        #δημιουργία γραφικών για τα κουμπιά της εφαρμογής
        button_frame = tk.Frame(self.w)
        button_frame.place(x=100, y=150)
        button_options = {'font': ("Arial", 20), 'width': 2, 'height': 1,'padx': 10, 'pady': 10, 'bg': '#3b3a3a', 'fg': 'white'}
        button_0 = tk.Button(button_frame, text='0', **button_options, command="")
        button_1 = tk.Button(button_frame, text="1", **button_options)
        button_2 = tk.Button(button_frame, text="2", **button_options)
        button_3 = tk.Button(button_frame, text="3", **button_options)
        button_4 = tk.Button(button_frame, text="4", **button_options)
        button_5 = tk.Button(button_frame, text="5", **button_options)
        button_6 = tk.Button(button_frame, text="6", **button_options)
        button_7 = tk.Button(button_frame, text="7", **button_options)
        button_8 = tk.Button(button_frame, text="8", **button_options)
        button_9 = tk.Button(button_frame, text="9", **button_options)
        button_neg = tk.Button(button_frame, text="+/-", **button_options)
        button_comma = tk.Button(button_frame, text=",", **button_options)

        # Use grid to place buttons in a grid layout
        button_7.grid(row=4, column=3)
        button_8.grid(row=4, column=4)
        button_9.grid(row=4, column=5)

        button_4.grid(row=5, column=3)
        button_5.grid(row=5, column=4)
        button_6.grid(row=5, column=5)

        button_1.grid(row=6, column=3)
        button_2.grid(row=6, column=4)
        button_3.grid(row=6, column=5)

        button_0.grid(row=7, column=4)

        button_neg.grid(row=7, column=5)
        button_comma.grid(row=7, column=3)

    def on_key_press(self,event):
        #αναγνωρίζει το input από το πληκτρολόγιο του χρήστη
        #το εισάγει στο entry widget
        self.key_pressed = event.char
        self.current_text = self.entry_box.get()
        self.entry_box.delete(0,tk.END)
        self.entry_box.insert(tk.END, self.current_text + self.key_pressed)

    def create_entry_box(self):
        self.entry_box = tk.Entry(self.w, justify='right',bg="#232323", fg='white', font=("Arial", 32))
        self.entry_box.pack(fill="x", padx=10, pady=10, ipadx=8, ipady=8)
        self.w.bind('<Key>', self.on_key_press)
    
    

w = tk.Tk()
calc_app = Calculator_App(w)
w.mainloop()
