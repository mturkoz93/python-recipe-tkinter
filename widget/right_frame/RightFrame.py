import tkinter as tk
from page.home_page.HomePage import HomePage
from page.shuffle_recipe.ShuffleRecipe import ShuffleRecipe
from page.create_recipe.CreateRecipe import CreateRecipe

from data.colors import COLORS

class RightFrame:

    def __init__(self, root, name, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=root,
            name=name,
            relief=relief,
            bg=COLORS.orange
        )
        self.side = side
        self.add_frame()

    def add_frame(self):
        self.frame_content()
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_content(self, page_name="homePage"):
        try:
            frame = self.frame
        except:
            frame = self
        finally:
            if page_name == "homePage":
                HomePage(frame, COLORS.root_bg_color)
            elif page_name == "shuffleRecipe":
                ShuffleRecipe(frame, COLORS.root_bg_color)
            elif page_name == "createRecipe":
                CreateRecipe(frame, COLORS.root_bg_color)
            elif page_name == "exit":
                frame.quit()

    def destroy_children(frame):
        # destroy frame children
        for child in frame.winfo_children():
            child.destroy()