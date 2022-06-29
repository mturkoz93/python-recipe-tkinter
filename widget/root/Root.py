import tkinter as tk
from data.colors import COLORS

ROOT_WIDTH = 960
ROOT_HEIGTH = 680

class Root:
    """
    root window
    """

    def __init__(self, title):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.configure(bg=COLORS.root_bg_color)
        self.set_height()

    def start_root(self):
        self.root.mainloop()

    def set_height(self):
        # place app in the center of the screen
        x = self.root.winfo_screenwidth() // 4
        y = int(self.root.winfo_screenheight() * 0.1)
        self.root.geometry(f'{ROOT_WIDTH}x{ROOT_HEIGTH}+' + str(x) + '+' + str(y))