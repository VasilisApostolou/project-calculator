import tkinter as tk
from tkinter import messagebox
import math as m


class Calculator_App():
        def __init__(self, w):
                #ορισμός μεταβλητών κλάσης
                self.current_calculation = ""
                self.w = w
                self.run_app()
        
        def create_tkinter_window(self):
                #συνάρτηση δημιουργίας του παραθύρου γραφικών
                self.w.geometry("380x500")
                self.w.title("SCIENTIFIC CALCULATOR")
                self.w.resizable(height=False, width=False)
                self.w.configure(bg='#3b3a3a')

        def run_app(self):
                #συνάρτηση η οποία καλεί τις υπόλοιπες βασικές συναρτήσεις του προγράμματος
                self.create_tkinter_window()
                self.create_buttons_grid()
                self.create_entry_box()
                self.create_option_menu()
                self.create_label()
                self.keyboard_binds()
         
        def create_buttons_grid(self):
                #δημιουργία γραφικών για τα κουμπιά της εφαρμογής
                self.button_frame = tk.Frame(self.w,bg="#3b3a3a")
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
                button_prcnt = tk.Button(self.button_frame, text="%", **button_options, command=self.percent)
                button_sqrt = tk.Button(self.button_frame, text="√", **button_options, command=self.calculate_sqrt)
                self.button_log = tk.Button(self.button_frame, text="log10",font=("Poppins",13),width=4,height=2,padx=4,pady=5,bg="#3b3a3a",fg="white" , command=self.calculate_log10)
                button_clear = tk.Button(self.button_frame,text="C", **button_options, command=self.clear_entry)
                button_del = tk.Button(self.button_frame,text="⌫", font=("Poppins",18),width=2,height=1,padx=8,pady=8,bg="#3b3a3a",fg="#a50000",command=self.delete)
                button_π = tk.Button(self.button_frame, text='π', **button_options, command=self.pi)
                button_ln = tk.Button(self.button_frame,text="ln",**button_options, command=self.calculate_ln)
                button_absolute = tk.Button(self.button_frame,text="|x|",**button_options, command=self.absolute)
                button_power2 = tk.Button(self.button_frame,text="x²", **button_options, command=self.calculate_x2)
                button_cos = tk.Button(self.button_frame,text="cos",**button_options, command=self.calculate_cos)
                button_sin = tk.Button(self.button_frame,text="sin",**button_options, command=self.calculate_sin)
                button_tan = tk.Button(self.button_frame,text="tan",**button_options,command=self.calculate_tan)
                button_e = tk.Button(self.button_frame,text="e",**button_options,command=self.e)
                button_xʸ=tk.Button(self.button_frame,text="xʸ",**button_options, command=self.power)
                button_bin = tk.Button(self.button_frame,text="Bin",**button_options, command=self.binary)
                button_oct = tk.Button(self.button_frame,text="Oct",**button_options, command=self.octal)
                button_hex = tk.Button(self.button_frame,text="Hex",**button_options, command=self.hexadecimal)
                button_par_l = tk.Button(self.button_frame, text='(', **button_options, command=self.right_par)
                button_par_r = tk.Button(self.button_frame, text=')', **button_options,command=self.left_par)
                button_mod = tk.Button(self.button_frame,text="mod", **button_options, command=self.mod)
                button_dec = tk.Button(self.button_frame, text="Dec",**button_options, command=self.decimal)
                button_exp = tk.Button(self.button_frame, text="exp",**button_options,command=self.exp)
                button_sinh = tk.Button(self.button_frame, text="sinh",**button_options, command=self.calculate_sinh)
                button_cosh = tk.Button(self.button_frame, text="cosh",**button_options,command=self.calculate_cosh)
                button_tanh = tk.Button(self.button_frame, text="tanh",**button_options, command=self.calculate_tanh)
                
                # Use grid to place buttons in a grid layout

                button_mod.grid(row=2,column=0)
                button_e.grid(row=2,column=1)
                button_absolute.grid(row=2,column=2)
                button_par_l.grid(row=2,column=3)
                button_par_r.grid(row=2,column=4)
                button_clear.grid(row=2,column=5)
                button_del.grid(row=2,column=6)
                
                button_power2.grid(row=3,column=0)
                button_π.grid(row=3,column=1)
                button_ln.grid(row=3,column=2)
                self.button_log.grid(row=3,column=3)
                button_sqrt.grid(row=3,column=4)
                button_prcnt.grid(row=3,column=5)
                button_div.grid(row=3,column=6)
                
                button_exp.grid(row=4,column=0)
                button_xʸ.grid(row=4,column=1)
                button_dec.grid(row=4,column=2)
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

        def create_label(self):
                #δημιουργεί την ετικέτα που γράφει Scientific Calculator
                self.label = tk.Label(self.w, text="SCIENTIFIC CALCULATOR", bg="#3b3a3a", fg="#00b8dd", font=("Poppins", 14))
                self.label.place(x=10,y=89)

        def create_entry_box(self):
                #δημιουργεί το display box για τους αριθμούς
                self.entry_box = tk.Entry(self.w, justify='right',bg="#232323", fg='white', font=("Poppins", 24))
                self.entry_box.pack(fill="x", padx=10, pady=10, ipadx=8, ipady=8)
                self.w.bind('<Key>', self.on_key_press)
        
        def create_option_menu(self):
                #δημιουργεί ένα μενού με επιλογές τις οποίες μπορεί να χρησιμοποιήσει ο χρήστης
                self.option_menu = tk.Menu(self.w)
                self.w.config(menu=self.option_menu)
                
                self.option_menu.add_command(label="Exit", command=self.exit_calc)
                self.resize_options = tk.Menu(self.option_menu, tearoff=0)
                self.resize_options.add_command(label="Bigger", command=self.resize_bigger)
                self.resize_options.add_command(label="Regular", command=self.resize_regular)
                self.option_menu.add_cascade(label="Resize",menu=self.resize_options)
        
        def exit_calc(self):
                #χρησιμοποιείται απο το option_menu και δίνει την επιλογή στον χρήστη να κλείσει το πρόγραμμα
                users_response = messagebox.askquestion("EXIT","Are you sure you want to exit the program?") #μήνυμα προειδοποιήσης 
                if users_response == "yes":
                        w.destroy()
        
        def resize_bigger(self):
                #μεγαλώνει το tkinter παράθυρο 
                #και μετακινέι το button_frame
                #χρήση για μεγαλύτερες οθόνες
                w.geometry("380x600")
                self.button_frame.place(x=23,y=130)
                for child in self.button_frame.winfo_children():
                        if isinstance(child, tk.Button):
                                child.configure(font=("Poppins", 14))
                self.button_log.config(font=("Poppins", 12))
                self.button_log.config(width=3,height=2)
                self.button_log.config(pady=2,padx=5)

        def resize_regular(self):
                #μετατρέπει το tkinter παράθυρο
                #στο αρχικό του μέγεθος
                w.geometry("380x500")
                self.button_frame.place(x=8, y=130)
                for child in self.button_frame.winfo_children():
                        if isinstance(child, tk.Button):
                                child.configure(font=("Poppins", 18))
                self.button_log.config(font=("Poppins", 13))
                self.button_log.config(width=4,height=2)
                self.button_log.config(pady=5,padx=4)
                
        def entry_size_configuration(self):
                #Το πρόγραμμα ελέγχει το μέγεθος του entry 
                #έτσι ώστε αμα τα ψηφία είναι πολλά και να μικραίνει 
                #η γραμματοσειρά των ψηφίων και να βλέπει ο χρήστης περισσότερα ψηφία
                if len(self.entry_box.get()) > 18:
                        self.entry_box.configure(font=("Poppins", 20))
                if len(self.entry_box.get()) > 21:
                        self.entry_box.configure(font=("Poppins", 16))
        
        def error_handling(self,error="Error-Invalid Input"):
                #συνάρτηση η οποία καλείται σε περίπτωση 
                #που ο χρήστης εισάγει κάτι το οποίο 
                #θα εμφανίσει error στο termminal 
                self.entry_box.configure(font=("Poppins", 22))
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,error)
        
        def on_key_press(self,event):
                #αναγνωρίζει το input από το πληκτρολόγιο του χρήστη
                #το εισάγει στο entry widget
                valid_keys = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '(', ')', '.'}
                if event.char in valid_keys:
                        self.key_pressed = event.char
                        self.current_calculation += self.key_pressed
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END, self.current_calculation)
                        self.entry_size_configuration()
        
        def keyboard_binds(self):
                self.w.bind('<Return>', lambda event=None: self.equalize())
                self.w.bind('<BackSpace>', lambda event=None: self.delete())
                self.w.bind('<e>', lambda event=None: self.e())
                self.w.bind('<p>', lambda event=None: self.pi())
        
        def press_btn(self,n):
                #αναγνωρίζει το πάτημα των κουμπιών 
                self.current_calculation += str(n)
                self.entry_box.delete(0, tk.END)
                self.entry_box.insert(tk.END, self.current_calculation)
        
        def equalize(self):
                #συνάρτηση η οποία χρησιμοποιεί την εντολή evaluate
                #δίνοντας το αποτέλεσμα στις βασικές πράξεις τις οποίες καλύπτει 
                #η εντολή eval()
                try:
                        self.calculated_text = eval(self.current_calculation)
                        self.entry_box.delete(0, tk.END)
                        self.entry_box.insert(tk.END, str(self.calculated_text))
                        self.current_calculation = str(self.calculated_text)
                        self.entry_size_configuration()
                except ZeroDivisionError:
                        self.entry_box.delete(0, tk.END)
                        self.entry_box.insert(tk.END, "Cannot divide by zero")
                        self.current_calculation = ""
                except:
                        self.error_handling()
                        self.current_calculation = ""               


        #στις παρακάτων συναρτήσεις περιέχεται η λειτουργία καθε κουμπιού 
        #στο calculator
        def clear_entry(self):
                self.current_calculation = ""
                self.entry_box.delete(0,tk.END)
                self.entry_box.configure(font=('Poppins',24))

        def delete(self):
                self.current_calculation = self.current_calculation[:-1]
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END, self.current_calculation)
        
        def calculate_log10(self):
                try:
                        self.number = float(self.current_calculation)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,m.log10(self.number))
                        self.current_calculation = str(m.log10(self.number))
                        self.entry_size_configuration()
                except:
                        self.error_handling()
                        self.current_calculation = ""
        
        def calculate_ln(self):
                try:
                        self.number = float(self.current_calculation)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,m.log(self.number))
                        self.current_calculation = str(m.log(self.number))
                        self.entry_size_configuration()
                except:
                        self.error_handling()
                        self.current_calculation = ""
                
    
        def calculate_sin(self):
                try:
                        self.number= float(self.current_calculation)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,m.sin(self.number))
                        self.current_calculation = str(m.sin(self.number))
                        self.entry_size_configuration()
                except:
                        self.error_handling()
                        self.current_calculation = ""
       
        def calculate_cos(self):
                try:
                        self.number=float(self.current_calculation)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,m.cos(self.number))
                        self.current_calculation = str(m.cos(self.number))
                        self.entry_size_configuration()
                except:
                        self.error_handling()
                        self.current_calculation = ""
        
        def calculate_tan(self):
                try:
                        self.number=float(self.current_calculation)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,m.tan(self.number))
                        self.current_calculation = str(m.tan(self.number))
                        self.entry_size_configuration()
                except:
                        self.error_handling()
                        self.current_calculation = ""       
        
        def calculate_sinh(self):
                try:
                        self.number=float(self.current_calculation)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,m.sinh(self.number))        
                        self.current_calculation = str(m.sinh(self.number))
                        self.entry_size_configuration()
                except:
                        self.error_handling()
                        self.current_calculation = ""               
        
        def calculate_cosh(self):
                try:
                        self.number=float(self.current_calculation)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,m.cosh(self.number))
                        self.current_calculation = str(m.cosh(self.number))
                        self.entry_size_configuration()
                except:
                        self.error_handling()
                        self.current_calculation = ""       
       
        def calculate_tanh(self):
                try:
                        self.number=float(self.current_calculation)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,m.tanh(self.number))
                        self.entry_size_configuration()
                except:
                        self.error_handling()
                        self.current_calculation = ""
        
        def calculate_sqrt(self):
                try:
                        self.number = float(self.current_calculation)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,m.sqrt(self.number))
                        self.current_calculation = str(m.sqrt(self.number))
                        self.entry_size_configuration()
                except:
                        self.error_handling()
                        self.current_calculation = ""
        
        def calculate_x2(self):
                try:
                        self.number = float(self.current_calculation)
                        self.number_power2 = self.number ** 2
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,self.number_power2)
                        self.current_calculation = str(self.number_power2)
                        self.entry_size_configuration()
                        self.entry_size_configuration()
                except:
                        self.error_handling()
                        self.current_calculation = ""
        
        def e(self):
                try:
                        self.current_calculation += str(m.e)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,self.current_calculation)
                except:
                        self.error_handling()
                        self.current_calculation = ""

        def pi(self):
                try:
                        self.current_calculation += str(m.pi)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,self.current_calculation)
                except:
                        self.error_handling()
                        self.current_calculation = ""
        
        def neg(self):
                try:
                        self.current_calculation = float(self.current_calculation)
                        self.negative_calc = -self.current_calculation
                        self.negative_calc = str(self.negative_calc)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,self.negative_calc)
                        self.current_calculation = self.negative_calc
                except:
                        self.error_handling()
                        self.current_calculation = ""
        
        def right_par(self):
                try:
                        self.current_calculation += "("
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,self.current_calculation)
                except:
                        self.error_handling()
                        self.current_calculation = ""
        
        def left_par(self):
                try:
                        self.current_calculation += ")"
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,self.current_calculation)
                except:
                        self.error_handling()
                        self.current_calculation = ""
        
        def absolute(self):
                try:
                        self.current_calculation = float(self.current_calculation)
                        self.abs_calc = abs(self.current_calculation)
                        self.abs_calc = str(self.abs_calc)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,self.abs_calc)
                        self.current_calculation = self.abs_calc
                except:
                        self.error_handling()
                        self.current_calculation = ""
        
        def binary(self):
                try:
                        self.current_calculation = int(self.current_calculation)
                        self.converted = bin(self.current_calculation)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,self.converted[2:])
                        self.current_calculation = ""
                        self.entry_size_configuration()
                except (ValueError, TypeError):
                        self.error_handling()
                        self.current_calculation = ""
        
        def octal(self):
                try:
                        self.current_calculation = int(self.current_calculation)
                        self.converted = oct(self.current_calculation)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,self.converted[2:])
                        self.current_calculation = ""      
                        self.entry_size_configuration()    
                except (ValueError, TypeError):
                        self.error_handling()
                        self.current_calculation = ""
        
        def hexadecimal(self):
                try:
                        self.current_calculation = int(self.current_calculation)
                        self.converted = hex(self.current_calculation)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,self.converted[2:])
                        self.current_calculation = ""      
                        self.entry_size_configuration()
                except (ValueError, TypeError):
                        self.error_handling()
                        self.current_calculation = ""
        
        def decimal(self):
                try:
                        self.converted = int(self.current_calculation, 2)
                        self.converted = str(self.converted)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,self.converted)
                        self.current_calculation = self.converted
                        self.entry_size_configuration()
                except ValueError:
                        self.entry_box.delete(0, tk.END)
                        self.entry_box.insert(tk.END,"Already a decimal")
                        self.current_calculation = ""
                except:
                        self.error_handling()
                        self.current_calculation = ""              

        def mod(self):
                try:
                        self.current_calculation += "%"
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,self.current_calculation)
                except:
                        self.error_handling()
                        self.current_calculation = ""
                
        def percent(self):
                try:
                        self.calculated_text = eval(self.current_calculation)
                        self.calculated_text = int(self.calculated_text)
                        self.prcnt = self.calculated_text * 0.01
                        self.entry_box.delete(0, tk.END)
                        self.entry_box.insert(tk.END, str(self.prcnt))
                        self.current_calculation = str(self.prcnt)
                except:
                        self.error_handling()
                        self.current_calculation = ""

        def power(self):
                try:
                        self.current_calculation += "**"
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,self.current_calculation)
                        self.entry_size_configuration()
                except:
                        self.error_handling()
                        self.current_calculation = ""

        def exp(self):
                try:
                        self.number = float(self.current_calculation)
                        self.exp_num = m.exp(self.number)
                        self.entry_box.delete(0,tk.END)
                        self.entry_box.insert(tk.END,self.exp_num)
                        self.entry_size_configuration()
                except OverflowError:
                        self.entry_box.delete(0, tk.END)
                        self.entry_box.insert(tk.END, "Result too large")
                        self.current_calculation = ""

                except:
                        self.error_handling()
                        self.current_calculation = ""                       


if __name__ == "__main__":
        w = tk.Tk()
        calc_app = Calculator_App(w)
        w.mainloop()
