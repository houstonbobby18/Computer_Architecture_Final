import tkinter as tk

import misc_functions as mf

class spinbox_window:
    def __init__(self, master, msg, spinbox_values):
        self.master = master
        self.master.title("Fruit Classifier")
        self.master.geometry("800x800")
        self.master.resizable(False, False)

        # Create a frame
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        # Create a label
        
        self.label = tk.Label(self.frame, text=msg)
        self.label.pack()

        # Create Dropdown menu 
        self.variable = tk.StringVar(self.master)
        self.variable.set(spinbox_values[0])
        self.dropdown = tk.OptionMenu(self.frame, self.variable, *spinbox_values)
        self.dropdown.pack()

        # Create a button
        self.button = tk.Button(self.frame, text="Submit", command=self.submit)
        self.button.pack()

    def submit(self):
        global returning_value
        returning_value = self.variable.get()
        self.master.destroy()

def get_fruit_name():
    global returning_value
    msg = "Please select the correct fruit: "
    spinbox_values = mf.get_fruit_index_names()
    root = tk.Tk()
    app = spinbox_window(root, msg, spinbox_values)
    root.mainloop()
    return returning_value

def get_storage_method():
    global returning_value
    msg = "How will the fruit be stored?"
    spinbox_values = ["Counter","Pantry","Fridge", "Freezer"]
    root = tk.Tk()
    app = spinbox_window(root, msg, spinbox_values)
    root.mainloop()
    return returning_value


if __name__ == "__main__":
    value = get_storage_method()
    print(value)