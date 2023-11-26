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
            button_frame.place(x=155, y=158)
            button_options = {'font': ("Poppins", 16), 'width': 2, 'height': 1,'padx': 8, 'pady': 8, 'bg': '#3b3a3a', 'fg': 'white'}
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
            button_equal = tk.Button(button_frame, text="=", **button_options)
            button_addit = tk.Button(button_frame, text="+", **button_options)
            button_subtr = tk.Button(button_frame, text="-", **button_options)
            button_mult = tk.Button(button_frame, text="×", **button_options)
            button_div = tk.Button(button_frame, text="÷", **button_options)
            button_prcnt = tk.Button(button_frame, text="%", **button_options)
            button_sqrt = tk.Button(button_frame, text="√", **button_options)
            button_log = tk.Button(button_frame, text="log", **button_options)
            button_clear = tk.Button(button_frame,text="CE", **button_options)
            button_del = tk.Button(button_frame,text="⌫", **button_options)
            button_e = tk.Button(button_frame, text='e', **button_options)
            button_π = tk.Button(button_frame, text='π', **button_options)
            button_ln = tk.Button(button_frame,text="ln",**button_options)
            button_absolute = tk.Button(button_frame,text="|x|",**button_options)
            # Use grid to place buttons in a grid layout
            button_absolute.grid(row=2,column=2)
            button_π.grid(row=2,column=3)
            button_e.grid(row=2,column=4)
            button_clear.grid(row=2,column=5)
            button_del.grid(row=2,column=6)
            
            
            button_ln.grid(row=3,column=2)
            button_log.grid(row=3,column=3)
            button_sqrt.grid(row=3,column=4)
            button_prcnt.grid(row=3,column=5)
            button_div.grid(row=3,column=6)

            button_7.grid(row=4, column=3)
            button_8.grid(row=4, column=4)
            button_9.grid(row=4, column=5)
            button_mult.grid(row=4,column=6)

            button_4.grid(row=5, column=3)
            button_5.grid(row=5, column=4)
            button_6.grid(row=5, column=5)
            button_subtr.grid(row=5,column=6)

            button_1.grid(row=6, column=3)
            button_2.grid(row=6, column=4)
            button_3.grid(row=6, column=5)
            button_addit.grid(row=6,column=6)
            
            button_comma.grid(row=7, column=3)
            button_0.grid(row=7, column=4)
            button_neg.grid(row=7, column=5)
            button_equal.grid(row=7, column=6)
    
    
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
