import tkinter as tk
from PIL import ImageTk

from data.colors import COLORS

class HomePage:

    def __init__(self, root, bg, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=root,
            name="homePage",
            relief=relief,
            bg=bg,
        )
        self.side = side
        self.frame_content()
        self.add_frame()

    def add_frame(self):
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_content(self):
        t = tk.Label(
            self.frame,
            text="Home Page",
            font=("Helvetica", 18, "bold"),
            bg=COLORS.orange,
        )
        # t.place(x=315, y=50)
        t.pack(fill=tk.X)

        self.load_logo()

        tk.Label(
            self.frame, 
            text="ready for your random recipe?",
            bg=COLORS.green,
            fg="white",
            font=("TkMenuFont", 14)
            ).pack(pady=20)

    def load_logo(self):
        # logo widget
        logo_img = ImageTk.PhotoImage(file="assets/Recipe_logo.png")
        logo_widget = tk.Label(self.frame, image=logo_img, bg=COLORS.root_bg_color)
        logo_widget.image = logo_img
        logo_widget.pack(pady=10)
        