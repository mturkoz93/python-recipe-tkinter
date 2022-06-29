import tkinter as tk


window = tk.Tk()
window.title('Tkinter Recipe App')
window.geometry('600x400+10+20') # "widthxheight+XPOS+YPOS"

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=400, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

label1 = tk.Label(master=frame2, text="I'm at (0, 0)", bg="blue", fg="white")
label1.place(x=1, y=0)

window.mainloop()