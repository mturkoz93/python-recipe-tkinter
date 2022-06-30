import tkinter as tk
from PIL import ImageTk

from widget import Root, LeftFrame
from widget.right_frame.RightFrame import RightFrame

# *************************************


# Root window
main_root = Root("Tkinter Recipe App")

# Left window
left_frame = LeftFrame(main_root.root, 'leftFrame')

# Right window
right_frame = RightFrame(main_root.root, 'rightFrame')

# Start mainloop
main_root.start_root()


# *************************************