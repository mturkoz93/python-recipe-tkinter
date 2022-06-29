import tkinter as tk
from numpy import random
import requests
from numpy import random

from data.colors import COLORS
from data.config import BASE_URL

class ShuffleRecipe:

    def __init__(self, master, bg, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=master,
            name="shuffleRecipe",
            relief=relief,
            bg=bg
        )
        self.side = side
        self.recipes = []
        
        self.add_frame()
        self.frame_content()

    def add_frame(self):
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_content(self):
        t = tk.Label(
            self.frame,
            text="Shuffle Recipe",
            font=("Helvetica", 18, "bold"),
            bg=COLORS.orange,
            fg=COLORS.black
        )
        t.pack(fill=tk.X, pady=(0, 30))

        tk.Label(
            self.frame, 
            text="Click the shuffle button for new recipe.",
            bg=COLORS.light_green,
            fg=COLORS.black,
            font=("TkMenuFont", 14)
            ).pack(pady=5)

        # button widget
        tk.Button(
            self.frame,
            text="SHUFFLE RECIPE",
            font=("TkHeadingFont", 20),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: self.random_recipe()
        ).pack(pady=20)

    def random_recipe(self):
        self.clear_widgets(self.frame)
        self.frame_content()

        datas = self.getRecipes()
        random_number = random.randint(0, len(datas))

        title, ingredients = self.pre_process(datas, random_number)

        tk.Label(
            self.frame, 
            text=title,
            bg=COLORS.green,
            fg="white",
            font=("TkHeadingFont", 20)
            ).pack(pady=25)

        for i in ingredients:
            tk.Label(
                self.frame, 
                text=i,
                bg=COLORS.green,
                fg="white",
                font=("TkMenuFont", 14)
                ).pack()


    def pre_process(self, datas, index):
        ingredients = []
        title = datas[index]["title"]
        steps = datas[index]["steps"]

        for step in steps:
            ingredients.append(step)

        return title, ingredients

    def getRecipes(self):
        url = BASE_URL + "recipes"
        response = requests.get(url)
        
        return response.json()

    def clear_widgets(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
