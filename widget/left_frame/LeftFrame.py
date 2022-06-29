import tkinter as tk
from data.colors import COLORS

class LeftFrame:

    def __init__(self, root, name):
        self.frame = tk.Frame(
            master=root,
            name=name,
            bg=COLORS.green
        )
        self.master = root
        self.add_frame()
        self.add_button()

    def add_frame(self):
        self.frame.pack(
            side=tk.LEFT,
            fill=tk.Y,
            pady=(62, 0)
        )

    def add_button(self):
        btn = tk.Button(master=self.frame, text="Button Left Frame")
        btn.pack()