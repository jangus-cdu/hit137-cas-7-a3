# Image View Class
# The View class is responsible for displaying the user interface and handling
# user input. It interacts with the Model and Controller to display data and
# receive user input. The View class is implemented using the Tkinter library.
# The View class contains methods to create and manage the user interface,
# load and display images, and handle user input. The View will update with
# changes to the Model and Controller.

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageView:

    def __init__(self, root):
        self.root = root  # The main Tkinter window.
        self.root.title("Main Window - ImageView")
        self.main_window_width = 800  # Width of the main window.
        self.main_window_height = 600  # Height of the main window.
        self.menu_frame = None  # Frame for the menu.
        self.controls_frame = None  # Frame for control buttons.
        self.status_bar_frame = None  # Frame for the status bar.
        self.image_frame_orignial = None  # Frame for the original image.
        self.image_frame_edited = None  # Frame for the deited image.

        # Buttons
        self.file_menu_button = None  # Button to open the file menu.
        self.open_image_button = None  # Button to open a file.
        self.crop_image_button = None  # Button to crop the image.
        self.rotate_image_button = None  # Button to rotate the image.
        self.quit_button = None  # Button to quit the application.

        # Labels
        self.image_label_original = None  # Original image.
        self.image_label_edited = None  # Edited image.
        self.image_path = None  # Path to the image file.
        self.image_status_label = None  # Label to display the image status.
        self.create_widgets()

    # Initialize and place widgets
    def create_widgets(self):
        # Main window
        self.root.config(width=self.main_window_width,
                         height=self.main_window_height, bg="skyblue")

        # Create frames
        self.menu_frame = tk.Frame(self.root, bg="lightgrey")
        self.menu_frame.pack(side="top", padx=5, pady=5, fill="x")

        self.controls_frame = tk.Frame(self.root, bg="lightgrey")
        self.controls_frame.pack(side="left")

        self.image_frame_original = tk.Frame(
            self.root, width=200, height=200, bg="lightpink")
        self.image_frame_original.pack(padx=5, pady=5, side="left")

        self.image_frame_edited = tk.Frame(
            self.root, width=200, height=200, bg="lightseagreen")
        self.image_frame_edited.pack(side="right", padx=5, pady=5)

        self.status_bar_frame = tk.Frame(
            self.root, bd=1, relief=tk.SUNKEN, bg="lightgoldenrod1")
        self.status_bar_frame.pack(side="bottom", padx=5, pady=5, fill="x")

        # Create buttons
        self.open_image_button = tk.Button(
            self.controls_frame, text="Open Image")
        self.open_image_button.pack()

        self.save_image_button = tk.Button(
            self.controls_frame, text="Save Image")
        self.save_image_button.pack()

        self.crop_image_button = tk.Button(
            self.controls_frame, text="Crop Image")
        self.crop_image_button.pack()

        self.rotate_image_button = tk.Button(
            self.controls_frame, text="Rotate Image")
        self.rotate_image_button.pack()

        self.quit_button = tk.Button(
            self.controls_frame, text="QUIT", fg="red", command=self.root.destroy)
        self.quit_button.pack()

        # Create a label to display the image once loaded and supplied by the Model
        self.image_label_original = tk.Label(
            self.image_frame_original, text="Image_Label_Original", bg="lightgrey")
        self.image_label_original.pack(padx=3, pady=3)

        self.image_label_edited = tk.Label(
            self.image_frame_edited, text="Image_Label_Edited", bg="lightgrey")
        self.image_label_edited.pack(padx=3, pady=3)

        self.file_menu_button = tk.Button(
            self.menu_frame, text="File Menu", bg="lightgrey")
        self.file_menu_button.pack(side="left")

        self.image_status_label = tk.Label(
            self.status_bar_frame, text="Image Status", anchor=tk.W, bg="lightgrey")
        self.image_status_label.pack(side=tk.LEFT, fill=tk.X)

    # Display the image
    def display_image(self, image):
        print(f"ImageView.display_image():Displaying image: {image}")
        self.image_label_original.configure(image=image)
        # keep a reference so the image doesn't disappear!
        self.image_label_original.image = image

    # Open a file dialog to select an image file
    def open_image_file(self, start_path="/") -> str:
        print("ImageView.open_image_file(): Opening file dialog...")
        print(f"ImageView.open_image_file(): Start path: {start_path}")
        file_path = filedialog.askopenfilename(
            initialdir=start_path, title="Select file", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
        print(f"Image_View.open_file(): Selected file: {file_path}")
        return file_path

    def update_image(self, image):
        # Update displayed image
        pass

    def show_message(self, message):
        # Display message to user
        pass

    # Get user input from the entry widget
    def get_input(self):
        return self.entry.get()

    # Set the display text
    def set_display(self, text):
        self.display.config(text=text)
