import tkinter as tk
from numpy import random

from data.colors import COLORS

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
            text="SHUFFLE",
            font=("TkHeadingFont", 20),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: self.random_recipe()
        ).pack(pady=20)

        tk.Label(
            self.frame, 
            text="---",
            bg=COLORS.green,
            fg="white",
            font=("TkMenuFont", 14)
            ).pack()

    def random_recipe(self):
        random_number = random.randint(0, 100)
        print("Random number: " + str(random_number))