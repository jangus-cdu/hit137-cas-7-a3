"""
Group Name: CAS/DAN 07
Group Members:
Jason Angus - S365855
Marco Giacomelli - S383510
Yoana Vasileva - S263707

HIT137 Assignment 2 Question 1
File: main.py

This is the main file for the Assignment 3 GUI.
"""

from os import name
import tkinter as tk
import application

# TODO: Create skeleton for Model View Controller (MVC) functionality


def main():
    print("HIT137 - Group Assignment 3")
    root = tk.Tk()
    app = application.Application(master=root)
    app.run()


if __name__ == '__main__':
    SystemExit(main())
