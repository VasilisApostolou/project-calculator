        def calculate_sin(self):
                self.number= int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.sin(self.number))
        def calculate_cos(self):
                self.number=int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.cos(self.number))
        def calculate_tan(self):
                self.number=int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.tan(self.number))
        def calculate_sinh(self):
                self.number=int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.sinh(self.number))        
        def calculate_cosh(self):
                self.number=int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.cosh(self.number))
        def calculate_tanh(self):
                self.number=int(self.current_calculation)
                self.entry_box.delete(0,tk.END)
                self.entry_box.insert(tk.END,m.tanh(self.number))
