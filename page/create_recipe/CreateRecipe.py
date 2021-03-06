import tkinter as tk
import requests

from data.colors import COLORS
from data.config import BASE_URL

class CreateRecipe:

    def __init__(self, master, bg, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=master,
            name="createRecipe",
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
            text="Create Recipe",
            font=("Helvetica", 18, "bold"),
            bg=COLORS.orange,
            fg=COLORS.black
        )
        t.pack(fill=tk.X, pady=(0, 30))

        # button widget
        tk.Button(
            self.frame,
            text="CREATE RECIPE",
            font=("TkHeadingFont", 20),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: self.create_recipe()
        ).pack(pady=20)

    def create_recipe(self):
        new_recipes = [
            # Turkish
            {
                "title": "Sigara Böreği",
                "steps": ["1 kilo yufka", "Yarım kilo lor", "Sıvı yağ", "Tuz", "Karabiber"]
            },
            {
                "title": "Sütsüz Kakaolu Islak Kek",
                "steps": ["1 su bardağı şeker", "4 yumurta", "2,5 su bardağı un", "1 su bardağı sıvı yağ", "3 yemek kaşığı kakao"]
            },
            {
                "title": "Patlıcanlı Talaş Böreği",
                "steps": ["3 adet günlük yufka", "3 adet patlıcan", "1 büyük soğan", "2 büyük domates rendesi", "2-3 yeşil biber"]
            },
            {
                "title": "Peynirli Susamlı Lezzet Topları",
                "steps": ["250 gr margarin", "2 yemek kaşığı toz şeker", "2 yemek kaşığı sirke", "2 yemek kaşığı sıvı yağ"]
            },
            {
                "title": "Fırında Patates Mücver",
                "steps": ["6 adet orta boy patates", "1 adet orta boy soğan", "3 adet yumurta", "1 çay bardağı sıvı yağ"]
            },
            # English
            {
                "title": "Cake Pie",
                "steps": ["1 kilo of dough", "Half kilo of curd", "Oil", "Salt", "Pepper"]
            },
            {
                "title": "Dairy Cocoa Wet Cake",
                "steps": ["1 cup sugar", "4 eggs", "2.5 cups flour", "1 cup oil", "3 tablespoons cocoa"]
            },
            {
                "title": "Aubergine Chip Pastry",
                "steps": ["3 daily phyllo dough", "3 eggplants", "1 large onion", "2 large tomatoes grated", "2-3 green peppers"]
            },
            {
                "title": "Cheese Sesame Flavor Balls",
                "steps": ["250 g margarine", "2 tablespoons granulated sugar", "2 tablespoons vinegar", "2 tablespoons oil"]
            },
            {
                "title": "Baked Potato Mucver",
                "steps": ["6 medium potatoes", "1 medium onion", "3 eggs", "1 tea glass of oil"]
            },
        ]
        try:
            url = BASE_URL + "recipes"

            for recipe in new_recipes:
                response = requests.post(url, json = recipe)
                print(response)
            
            return True
        except Exception as ex:
            print(ex)
            return False

    def clear_widgets(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
