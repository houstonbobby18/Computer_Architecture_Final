import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

from PIL import Image, ImageTk

import fruit_name_model
import misc_functions as mf
import spinbox_window
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

possible_fruits = mf.get_fruit_index_names()

class user_interface_window:
    def __init__(self, master):
        self.master = master
        self.master.title("Fruit Classifier")
        self.master.geometry("800x800")
        self.master.resizable(False, False)
        self.real_fruit = ""

        # Create a frame
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        # Create a label
        self.label = tk.Label(self.frame, text="Upload a photo of a fruit")
        self.label.pack()

        # Create a button
        self.button = tk.Button(self.frame, text="Upload", command=self.upload)
        self.button.pack()

        self.button2 = tk.Button(self.frame, text="Submit", command=self.submit)
        self.button2.pack()

    def upload(self):
        self.filename = tk.filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        self.image = Image.open(self.filename)
        self.image.thumbnail((300, 300))
        self.photo = ImageTk.PhotoImage(self.image)
        self.label2 = tk.Label(self.frame, image=self.photo)
        self.label2.pack()
        guessed_fruit = fruit_name_model.run_model(self.filename)
        msg = f"Detected fruit: {guessed_fruit}\nIs the detected fruit correct?"
        # Creates msg box
        result = messagebox.askyesno("Fruit Classifier", msg)
        if result:
            self.real_fruit = guessed_fruit
        else:
            self.real_fruit = spinbox_window.get_fruit_name()

    def submit(self):
        storage_method = spinbox_window.get_storage_method()
        print(f"Real fruit: {self.real_fruit}")
        print(f"Storage method: {storage_method}")


root = tk.Tk()
app = user_interface_window(root)
root.mainloop()
