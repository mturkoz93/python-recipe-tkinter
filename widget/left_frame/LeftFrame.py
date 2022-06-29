import tkinter as tk
from data.colors import COLORS
from data.menus import MENU

from widget.button.Button import Button

class LeftFrame:

    def __init__(self, root, name):
        self.frame = tk.Frame(
            master=root,
            name=name,
            bg=COLORS.green
        )
        self.master = root
        self.add_frame()
        self.add_menus()

    def add_frame(self):
        self.frame.pack(
            side=tk.LEFT,
            fill=tk.Y,
            pady=(0, 0)
        )

    # event comes from button click
    def handle_click(self, event):
        self.manage_button_colors(event)

    def add_menus(self):
        # add with loop
        for menu_key, menu_text in MENU.items():
            if menu_key == "exit":
                button = Button(
                    self.frame, 
                    menu_key, 
                    menu_text, 
                    COLORS.orange, 
                    COLORS.black,
                    18, 2,
                    self.handle_click, 
                    0, 0, tk.BOTTOM
                    )
            else:
                button = Button(
                    self.frame, 
                    menu_key, 
                    menu_text, 
                    COLORS.orange, 
                    COLORS.black,
                    18, 2,
                    self.handle_click
                    )

    def manage_button_colors(self, event):
        # clicked button : event.widget
        # make black all buttons
        for child in event.widget.master.winfo_children():
            child.configure(bg=COLORS.black, fg=COLORS.orange)
        
        # change selected button color
        LeftFrame.set_selected_button_color(event.widget)


    def set_selected_button_color(button):
        button.configure(bg=COLORS.orange, fg=COLORS.white)