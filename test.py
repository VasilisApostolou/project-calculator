import tkinter as tk

# Create the main window
window = tk.Tk()

# Create the menu bar
menu_bar = tk.Menu(window)

# Create a menu "Menu1" in menu bar
menu_1 = tk.Menu(menu_bar, tearoff=0)

# Create Submenu
submenu_1 = tk.Menu(menu_1, tearoff=0)

# Add items to Submenu
submenu_1.add_command(label="Item3")
submenu_1.add_command(label="Item4")
submenu_1.add_command(label="Item5")

# Add items to Menu1
menu_1.add_command(label="Item1")
menu_1.add_command(label="Item2")
menu_1.add_cascade(label="SubMenu1", menu=submenu_1)

# Add the menu "Menu1" to the menu bar
menu_bar.add_cascade(label="Menu1", menu=menu_1)

# Attach the menu bar to the main window
window.config(menu=menu_bar)

# Start the Tkinter event loop
window.mainloop()