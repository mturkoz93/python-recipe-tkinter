import tkinter as tk
from PIL import ImageTk
import requests


bg_colour = "#3d6466"

def load_frame1():
    frame1.pack_propagate(False)
    # logo widget
    logo_img = ImageTk.PhotoImage(file="assets/Recipe_logo.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()


    # instructions widget
    tk.Label(
        frame1, 
        text="ready for your random recipe?",
        bg=bg_colour,
        fg="white",
        font=("TkMenuFont", 14)
        ).pack()

    # button widget
    tk.Button(
        frame1,
        text="SHUFFLE",
        font=("TkHeadingFont", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame2()
    ).pack(pady=20)

def load_frame2():
    print("Hello mustafa")


# initiallize app
root = tk.Tk()

root.title("Tkinter Recipe App")
# root.eval("tk::PlaceWindow . center")
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry('500x600+' + str(x) + '+' + str(y))
# root.geometry('600x400+10+20') # "widthxheight+XPOS+YPOS"

# create a frame widget
frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

load_frame1()


def getRecipes():
    url = "https://adesso-recipe-flask.herokuapp.com/recipes"
    response = requests.get(url)
    
    return response.json()

# label1.configure(text=getRecipes()[0]["steps"])


# run app
root.mainloop()