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
        self.random_number = -1
        
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
        try:
            
            datas = self.getRecipes()

            new_random_number = random.randint(0, len(datas))
            print("new_random_number: " + str(new_random_number))
            print("self_random_number: " + str(self.random_number))

            if str(new_random_number) == str(self.random_number):
                self.random_recipe()
                return False

            self.random_number = new_random_number

            title, ingredients = self.pre_process(datas, self.random_number)
            
            self.clear_widgets(self.frame)
            self.frame_content()

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
                    bg="#28393a",
                    fg="white",
                    font=("TkMenuFont", 14)
                    ).pack(fill="both")
        except Exception as ex:
            print(ex)
            return False


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
        print(response.text)
        print("Status code: " + str(response.status_code))

        if response.status_code != 200:
            print("There is an error!")
            raise
        
        return response.json()

    def clear_widgets(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
