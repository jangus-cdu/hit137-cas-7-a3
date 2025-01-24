import tkinter as tk

"""
Main Application
The Application class definition creates a GUI application using the tkinter 
library.
"""


class Application(tk.Frame):
    def __init__(self, master=None):
        """
        Initializes the Application frame.

        Initializes the application, setting the master window and packing the frame. It also calls the create_widgets method to set up the GUI components.

        Parameters:
            master (tk.Tk, optional): The root window or master widget. Defaults to None.

        Sets up the master window, packs the frame, and initializes the GUI components by calling create_widgets.
        """

        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the GUI components.

        Creates a single "QUIT" button with red text, which destroys the master window when clicked. The button is packed at the bottom of the frame.
        """
        self.quit_button = tk.Button(
            self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit_button.pack(side="bottom")

    def run(self):
        """
        Starts the application's main event loop, which waits for user interactions and updates the GUI.
        """
        self.mainloop()
