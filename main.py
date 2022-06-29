import tkinter as tk
from PIL import ImageTk
import requests
from numpy import random

from widget import Root
from data.config import BASE_URL


def method1():
    frame1 = tk.Frame(master=root, width=200, height=100, bg="red")
    frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    # frame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    frame2 = tk.Frame(master=root, width=100, bg="yellow")
    frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    label1 = tk.Label(master=frame1, text="I'm at (0, 0)", bg="blue", fg="white")
    label1.place(x=1, y=0)

    # logo widget
    logo_img = ImageTk.PhotoImage(file="assets/Recipe_logo.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg="green")
    logo_widget.image = logo_img
    logo_widget.pack()


    # instructions widget
    tk.Label(
        frame1, 
        text="ready for your random recipe?",
        bg="green",
        fg="white",
        font=("TkMenuFont", 14)
        ).pack()

    # button widget
    tk.Button(
        frame1,
        text="SHUFFLE",
        font=("TkHeadingFont", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame2()
    ).pack(pady=20)

def method2():
    random_number = random.randint(0, 100)
    print("Random number: " + str(random_number))

def getRecipes():
    url = BASE_URL + "recipes"
    response = requests.get(url)
    
    return response.json()


# *************************************


# Root window
root = Root("Tkinter Recipe App")

# Left window

# Right window

# Start mainloop
root.start_root()


# *************************************