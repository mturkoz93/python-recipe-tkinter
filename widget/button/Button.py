import tkinter as tk
from data.colors import COLORS


class Button:
    """
    creates button
    """

    def __init__(
        self, 
        master, 
        name, 
        text, 
        fg, bg, width, height, 
        handle_click,
        padx=0, pady=0,
        side=tk.TOP,
        ):
        self.button = tk.Button(
            master=master,
            name=name,
            text=text,
            fg=fg,
            bg=bg,
            width=width,
            height=height,
            activebackground=COLORS.button_active_bg_color,
            activeforeground=COLORS.button_active_fg_color
        )
        self.padx = padx
        self.pady = pady
        self.side = side
        self.add_button()
        self.event_bind(handle_click)

    def add_button(self):
        self.button.configure(font=("Arial", 12))
        self.button.pack(
            padx = self.padx,
            pady = self.pady,
            side = self.side
        )

    def event_bind(self, handle_click):
        self.button.bind("<Button-1>", handle_click)