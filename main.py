"""
Group Name: CAS/DAN 07
Group Members:
Jason Angus - S365855
Marco Giacomelli - S383510
Yoana Vasileva - S263707

HIT137 Assignment 3 - Image Editor
File: main.py

This is the main file for the Assignment 3 Image Editor Application.
"""

import tkinter as tk
import Image_Model
import Image_View
import Image_Controller

# TODO: Use OpenCV for image processing tasks. (Wed 29 Jan 2025)
# TODO: Add image resize slider and functionality. (Wed 29 Jan 2025)

if __name__ == '__main__':
    print("HIT137 - Group Assignment 3")
    root = tk.Tk()
    model = Image_Model.ImageModel()
    view = Image_View.ImageView(root)
    controller = Image_Controller.ImageController(model, view)
    view.controller = controller
    root.title("HIT137 - Image Editor")
    root.mainloop()
