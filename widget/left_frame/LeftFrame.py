import tkinter as tk
from data.colors import COLORS
from data.menus import MENU

from widget.button.Button import Button
from widget.right_frame.RightFrame import RightFrame

class LeftFrame:

    def __init__(self, root, name):
        self.frame = tk.Frame(
            master=root,
            name=name,
            bg=COLORS.gray
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
        page_name = str(event.widget).split(".")[2]

        # get right frame
        rightFrame = self.master.children["rightFrame"]
        # destroy children of rightFrame
        RightFrame.destroy_children(rightFrame)
        # open a page
        RightFrame.frame_content(rightFrame, page_name)


    def add_menus(self):
        # add with loop
        for menu_key, menu_text in MENU.items():
            if menu_key == "exit":
                button = Button(
                    self.frame, 
                    menu_key, 
                    menu_text, 
                    COLORS.white,
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
                    COLORS.white, 
                    COLORS.green,
                    18, 2,
                    self.handle_click
                    )

    def manage_button_colors(self, event):
        # clicked button : event.widget
        # make black all buttons
        for child in event.widget.master.winfo_children():
            if str(child) == ".leftFrame.exit":
                pass
            else:
                child.configure(bg=COLORS.green, fg=COLORS.white)
        
        # change selected button color
        LeftFrame.set_selected_button_color(event.widget)


    def set_selected_button_color(button):
        button.configure(bg=COLORS.orange, fg=COLORS.black)