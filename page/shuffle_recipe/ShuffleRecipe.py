import tkinter as tk
from tkinter import ttk
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
        )
        # t.place(x=315, y=50)
        t.pack(fill=tk.X)

    def create_recipe_card(self):
        pass