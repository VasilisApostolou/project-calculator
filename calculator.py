import tkinter as tk
import math


class Calculator_App():
      def __init__(self,w):
            self.w = w
            w.geometry("400x500")
            w.title("SCIENTIFIC CALCULATOR")
            w.resizable(height=False, width=False)
            self.create_buttons_grid()
            w.configure(bg='#3b3a3a')  # Grey background color
            

      def create_buttons_grid(self):
            button_options = {'font': ("Arial", 20), 'width': 2, 'height': 1, 'padx': 10, 'pady': 10, 'bg': '#3b3a3a', 'fg': 'white'}
            button_0 = tk.Button(self.w, text='0', **button_options)
            button_1 = tk.Button(self.w, text="1", **button_options)
            button_2 = tk.Button(self.w, text="2", **button_options)
            button_3 = tk.Button(self.w, text="3", **button_options)
            button_4 = tk.Button(self.w, text="4", **button_options)
            button_5 = tk.Button(self.w, text="5", **button_options)
            button_6 = tk.Button(self.w, text="6", **button_options)
            button_7 = tk.Button(self.w, text="7", **button_options)
            button_8 = tk.Button(self.w, text="8", **button_options)
            button_9 = tk.Button(self.w, text="9", **button_options)
            button_neg = tk.Button(self.w, text="+/-", **button_options)
            button_comma = tk.Button(self.w, text=",", **button_options)

            # Use grid to place buttons in a grid layout
            button_7.grid(row=0, column=0)
            button_8.grid(row=0, column=1)
            button_9.grid(row=0, column=2)

            button_4.grid(row=1, column=0)
            button_5.grid(row=1, column=1)
            button_6.grid(row=1, column=2)

            button_1.grid(row=2, column=0)
            button_2.grid(row=2, column=1)
            button_3.grid(row=2, column=2)

            button_0.grid(row=3, column=1)

            button_neg.grid(row=3, column=2)
            button_comma.grid(row=3, column=0)




w = tk.Tk()
calc_app = Calculator_App(w)
w.mainloop()
