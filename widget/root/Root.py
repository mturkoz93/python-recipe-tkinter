import tkinter as tk

class Root:
    """
    root window
    """

    def __init__(self, title):
        self.root = tk.Tk()
        self.root.title(title)

        # place app in the center of the screen
        x = self.root.winfo_screenwidth() // 2
        y = int(self.root.winfo_screenheight() * 0.1)
        self.root.geometry('500x600+' + str(x) + '+' + str(y))

    def start_root(self):
        self.root.mainloop()