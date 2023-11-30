import tkinter as tk
from tkinter import messagebox
import math as m

class Calculator_App():
        def __init__(self, w):
                #δημιουργία γραφικών παραθύρου εφαρμογής
                self.current_calculation = ""
                self.w = w
                self.w.geometry("380x500")
                self.w.title("SCIENTIFIC CALCULATOR")
                self.w.resizable(height=False, width=False)
                self.w.configure(bg='#3b3a3a')
                self.create_buttons_grid()
                self.create_entry_box()
                self.create_option_menu()
                
        def create_buttons_grid(self):
                #δημιουργία γραφικών για τα κουμπιά της εφαρμογής
                self.button_frame = tk.Frame(self.w)
                self.button_frame.place(x=8, y=130)
                button_options = {'font': ("Poppins", 18), 'width': 2, 'height': 1,'padx': 8, 'pady': 8, 'bg': '#3b3a3a', 'fg': 'white'}
                modified_button_options = button_options.copy()
                modified_button_options['bg'] = '#4b4e4f'
                button_0 = tk.Button(self.button_frame, text='0', **modified_button_options, command=lambda: self.press_btn('0'))
                button_1 = tk.Button(self.button_frame, text="1", **modified_button_options, command=lambda: self.press_btn('1'))
                button_2 = tk.Button(self.button_frame, text="2", **modified_button_options, command=lambda: self.press_btn('2'))
                button_3 = tk.Button(self.button_frame, text="3", **modified_button_options, command=lambda: self.press_btn('3'))
                button_4 = tk.Button(self.button_frame, text="4", **modified_button_options, command=lambda: self.press_btn('4'))
                button_5 = tk.Button(self.button_frame, text="5", **modified_button_options, command=lambda: self.press_btn('5'))
                button_6 = tk.Button(self.button_frame, text="6", **modified_button_options, command=lambda: self.press_btn('6'))
                button_7 = tk.Button(self.button_frame, text="7", **modified_button_options, command=lambda: self.press_btn('7'))
                button_8 = tk.Button(self.button_frame, text="8", **modified_button_options, command=lambda: self.press_btn('8'))
                button_9 = tk.Button(self.button_frame, text="9", **modified_button_options, command=lambda: self.press_btn('9'))
                button_neg = tk.Button(self.button_frame, text="+/-", **button_options,command=self.neg)
                button_comma = tk.Button(self.button_frame, text=",", **button_options,command=lambda: self.press_btn('.'))
                button_equal = tk.Button(self.button_frame, text="=", font=("Poppins",18),width=2,height=1,padx=8,pady=8,bg="#0a85b2",fg="white", command =lambda: self.equalize())
                button_addit = tk.Button(self.button_frame, text="+", **button_options,command=lambda: self.press_btn('+'))
                button_subtr = tk.Button(self.button_frame, text="-", **button_options,command=lambda: self.press_btn('-'))
                button_mult = tk.Button(self.button_frame, text="×", **button_options,command=lambda: self.press_btn('*'))
                button_div = tk.Button(self.button_frame, text="÷", **button_options,command=lambda: self.press_btn('/'))
                button_prcnt = tk.Button(self.button_frame, text="%", **button_options)
                button_sqrt = tk.Button(self.button_frame, text="√", **button_options, command=self.calculate_sqrt)
                button_log = tk.Button(self.button_frame, text="log10", **button_options, command=self.calculate_log10)
                button_clear = tk.Button(self.button_frame,text="C", **button_options, command=self.clear_entry)
                button_del = tk.Button(self.button_frame,text="⌫", font=("Poppins",18),width=2,height=1,padx=8,pady=8,bg="#3b3a3a",fg="#a50000",command=self.delete)
                button_π = tk.Button(self.button_frame, text='π', **button_options, command=self.pi)
                button_ln = tk.Button(self.button_frame,text="ln",**button_options, command=self.calculate_ln)
                button_absolute = tk.Button(self.button_frame,text="|x|",**button_options)
                button_power2 = tk.Button(self.button_frame,text="x²", **button_options, command=self.calculate_x2)
                button_cos = tk.Button(self.button_frame,text="cos",**button_options, command=self.calculate_cos)
                button_sin = tk.Button(self.button_frame,text="sin",**button_options, command=self.calculate_sin)
                button_tan = tk.Button(self.button_frame,text="tan",**button_options,command=self.calculate_tan)
                button_e = tk.Button(self.button_frame,text="e",**button_options,command=self.e)
                button_xʸ=tk.Button(self.button_frame,text="xʸ",**button_options)
                button_bin = tk.Button(self.button_frame,text="Bin",**button_options)
                button_oct = tk.Button(self.button_frame,text="Oct",**button_options)
                button_hex = tk.Button(self.button_frame,text="Hex",**button_options)
                button_par1 = tk.Button(self.button_frame, text='(', **button_options)
                button_par = tk.Button(self.button_frame, text=')', **button_options)
                button_mod = tk.Button(self.button_frame,text="mod", **button_options)
                button_gamma = tk.Button(self.button_frame, text="Γ(z)",**button_options, command=self.calculate_gamma)
                button_exp = tk.Button(self.button_frame, text="exp",**button_options)
                button_sinh = tk.Button(self.button_frame, text="sinh",**button_options, command=self.calculate_sinh)
                button_cosh = tk.Button(self.button_frame, text="cosh",**button_options,command=self.calculate_cosh)
                button_tanh = tk.Button(self.button_frame, text="tanh",**button_options, command=self.calculate_tanh)
                
                # Use grid to place buttons in a grid layout

                button_mod.grid(row=2,column=0)
                button_e.grid(row=2,column=1)
                button_absolute.grid(row=2,column=2)
                button_par1.grid(row=2,column=3)
                button_par.grid(row=2,column=4)
                button_clear.grid(row=2,column=5)
                button_del.grid(row=2,column=6)
                
                button_gamma.grid(row=3,column=0)
                button_π.grid(row=3,column=1)
                button_ln.grid(row=3,column=2)
                button_log.grid(row=3,column=3)
                button_sqrt.grid(row=3,column=4)
                button_prcnt.grid(row=3,column=5)
                button_div.grid(row=3,column=6)
                
                button_exp.grid(row=4,column=0)
                button_xʸ.grid(row=4,column=1)
                button_power2.grid(row=4,column=2)
                button_7.grid(row=4, column=3)
                button_8.grid(row=4, column=4)
                button_9.grid(row=4, column=5)
                button_mult.grid(row=4,column=6)
                
                button_sinh.grid(row=5,column=0)
                button_bin.grid(row=5,column=2)
                button_cos.grid(row=5,column=1)
                button_4.grid(row=5, column=3)
                button_5.grid(row=5, column=4)
                button_6.grid(row=5, column=5)
                button_subtr.grid(row=5,column=6)
                
                button_cosh.grid(row=6,column=0)
                button_oct.grid(row=6,column=2)
                button_sin.grid(row=6,column=1)
                button_1.grid(row=6, column=3)
                button_2.grid(row=6, column=4)
                button_3.grid(row=6, column=5)
                button_addit.grid(row=6,column=6)
                
                button_tanh.grid(row=7,column=0)
                button_hex.grid(row=7,column=2)
                button_tan.grid(row=7,column=1)
                button_comma.grid(row=7, column=3)
                button_0.grid(row=7, column=4)
                button_neg.grid(row=7, column=5)
                button_equal.grid(row=7, column=6)

        def create_entry_box(self):
                #δημιουργεί το display box για τους αριθμούς
                self.entry_box = tk.Entry(self.w, justify='right',bg="#232323", fg='white', font=("Arial", 32))
                self.entry_box.pack(fill="x", padx=10, pady=10, ipadx=8, ipady=8)
                self.w.bind('<Key>', self.on_key_press)
        
        def on_key_press(self,event):
                #αναγνωρίζει το input από το πληκτρολόγιο του χρήστη
                #το εισάγει στο entry widget
                self.key_pressed = event.char
                self.current_text = self.entry_box.get()
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END, self.current_text + self.key_pressed)
                print(self.key_pressed)

        def press_btn(self,n):
                self.current_calculation += str(n)
                self.entry_box.delete(0, tk.END)
                self.entry_box.insert(tk.END, self.current_calculation)

        def equalize(self):
                try:
                        self.calculated_text = eval(self.current_calculation)
                        print(self.calculated_text)
                        self.entry_box.delete(0, tk.END)
                        self.entry_box.insert(tk.END, str(self.calculated_text))
                        self.current_calculation = str(self.calculated_text)
                except:
                        self.entry_box.delete(0, tk.END)
                        self.entry_box.insert(tk.END, "Error-Invalid Input")
                        self.current_calculation = ""

        def exit_calc(self):
                #χρησιμοποιείται απο το option_menu και δίνει την επιλογή στον χρήστη να κλείσει το πρόγραμμα
                users_response = messagebox.askquestion("EXIT","Are you sure you want to exit the program?") #μήνυμα προειδοποιήσης 
                if users_response == "yes":
                        w.destroy()
        
        def resize(self):
                #μεγαλώνει το tkinter παράθυρο 
                #και μετακινέι το button_frame
                w.geometry("400x670")
                self.button_frame.place(x=19,y=130)
                
        def create_option_menu(self):
                #δημιουργεί ένα μενού με επιλογές τις οποίες μπορεί να χρησιμοποιήσει ο χρήστης
                self.option_menu = tk.Menu(self.w)
                self.w.config(menu=self.option_menu)
                self.option_menu.add_command(label="Resize", command=self.resize)
                self.option_menu.add_command(label="Exit", command=self.exit_calc)

        def calculate_log10(self):
                self.number = int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.log10(self.number))
                self.current_calculation = str(m.log10(self.number))
        
        def calculate_ln(self):
                self.number = int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.log(self.number))
                self.current_calculation = str(m.log(self.number))
                
        def clear_entry(self):
                self.current_calculation = ""
                self.entry_box.delete(0,tk.END)

        def delete(self):
                self.current_calculation = self.current_calculation[:-1]
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END, self.current_calculation)
                
        def calculate_sin(self):
                self.number= int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.sin(self.number))
                self.current_calculation = str(m.sin(self.number))
        
        def calculate_cos(self):
                self.number=int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.cos(self.number))
                self.current_calculation = str(m.cos(self.number))
        
        def calculate_tan(self):
                self.number=int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.tan(self.number))
                self.current_calculation = str(m.tan(self.number))
        
        def calculate_sinh(self):
                self.number=int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.sinh(self.number))        
                self.current_calculation = str(m.sinh(self.number))
        
        def calculate_cosh(self):
                self.number=int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.cosh(self.number))
                self.current_calculation = str(m.cosh(self.number))
        
        def calculate_tanh(self):
                self.number=int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.tanh(self.number))

        def calculate_sqrt(self):
                self.number = int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.sqrt(self.number))
                self.current_calculation = str(m.sqrt(self.number))
        
        def calculate_gamma(self):
                self.number = int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.gamma(self.number))
                self.current_calculation = str(m.gamma(self.number))
                
        def calculate_x2(self):
                self.number = int(self.current_calculation)
                self.number_power2 = self.number ** 2
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,self.number_power2)
                self.current_calculation = str(self.number_power2)

        def e(self):
                self.current_calculation = str(m.e)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,self.current_calculation)

        def pi(self):
                self.current_calculation = str(m.pi)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,self.current_calculation)

        def neg(self):
                self.current_calculation = int(self.current_calculation)
                self.negative_calc = -self.current_calculation
                self.negative_calc = str(self.negative_calc)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,self.negative_calc)

m.e    
w = tk.Tk()
calc_app = Calculator_App(w)
w.mainloop()
