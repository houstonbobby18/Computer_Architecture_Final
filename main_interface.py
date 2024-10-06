import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

from PIL import Image, ImageTk

import fruit_name_model
import misc_functions as mf
import fruit_duration as fd
import fruit_inventory as fi

# GitHub Copilot was used alongside the creation of this project.

'''
Objectives of this GUI:
-Allow the user to upload a photo and have it displayed on the screen.
-Copy the file to a new location.
-Store the new location.
-Run the photo through a fruit classifier.
-Display the results of the classifier.
-Ask the user for the correct classification.
-Store both values in a variable.
-Ask the user for how the fruit will be stored.
-Store the value in a variable.
-Get the expiration date of the fruit, from a database.
-Store the value in a variable.
-Load the Values into a database.
-Repeate the process.
'''
class user_interface_window:
    def __init__(self, master):
        self.possible_fruits = mf.get_fruit_index_names()
        self.master = master
        self.master.title("Fruit Classifier Database")
        self.master.geometry("800x800")
        self.master.resizable(False, False)
        self.storage_methods = ["Counter", "Pantry", "Fridge", "Freezer"]
        self.fruit_duration = fd.fruit_table()
        # Create a frame
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        # Load test image
        self.filename = r"new_files\\test.jpg"
        self.image = Image.open(self.filename)
        self.image.thumbnail((300, 300))
        self.photo = ImageTk.PhotoImage(self.image)
        self.gui_image = tk.Label(self.frame, image=self.photo)
        self.gui_image.grid(row=0, column=1)

        # Create upload button
        self.button = tk.Button(self.frame, text="Upload", command=self.upload)
        self.button.grid(row=1, column=1)

        # Create Fruit Name Option Menu
        self.fruit_name = tk.StringVar(self.master)
        self.fruit_name.set(self.possible_fruits[0])
        self.fruit_name_label = tk.Label(self.frame, text="Please select the correct fruit: ")
        self.fruit_name_label.grid(row=2, column=0)
        self.fruit_name_dropdown = tk.OptionMenu(self.frame, self.fruit_name, *self.possible_fruits)
        self.fruit_name_dropdown.grid(row=3, column=0)

        # Create Storage Method Option Menu
        self.storage_method = tk.StringVar(self.master)
        self.storage_method.set(self.storage_methods[0])
        self.storage_method_label = tk.Label(self.frame, text="How will the fruit be stored?")
        self.storage_method_label.grid(row=2, column=1)
        self.storage_method_dropdown = tk.OptionMenu(self.frame, self.storage_method, *self.storage_methods)
        self.storage_method_dropdown.grid(row=3, column=1)

        # Create Submit Button
        self.submit_button = tk.Button(self.frame, text="Submit", command=self.submit)
        self.submit_button.grid(row=3, column=2)

    def upload(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.image = Image.open(self.filename)
        self.image.thumbnail((300, 300))
        self.photo = ImageTk.PhotoImage(self.image)
        self.gui_image = tk.Label(self.frame, image=self.photo)
        self.gui_image.grid(row=0, column=1)
        guessed_fruit = fruit_name_model.run_model(self.filename)
        msg = f"Detected fruit: {guessed_fruit}\nIs the detected fruit correct?"
        # Creates msg box
        result = messagebox.askyesno("Fruit Classifier", msg)
        if result:
            self.fruit_name.set(guessed_fruit)

    def submit(self):
        # Get the values from the option menus
        fruit_name = self.fruit_name.get()
        storage_method = self.storage_method.get()
        storage_method = self.storage_methods.index(storage_method)
        expiration_date = self.fruit_duration.get_duration_values(fruit_name)[storage_method]
        guessed_fruit = fruit_name_model.run_model(self.filename)
        # Load the values into a database
        conn , cursor = fi.connect_database()
        fruit_id = fi.add_fruit(conn, cursor, self.filename, expiration_date, guessed_fruit, fruit_name)

root = tk.Tk()
app = user_interface_window(root)
root.mainloop()

# Create Message Box
result = messagebox.askyesno("Export Database", "Would you like to export the database?")
if result:
    if os.path.exists("fruit_database.csv"):
        os.remove("fruit_database.csv")
    conn , cursor = fi.connect_database()
    fi.export_database(conn, cursor)
    messagebox.showinfo("Export Database", "Database has been exported to 'fruit_database.csv'")

