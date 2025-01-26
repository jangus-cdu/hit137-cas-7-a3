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
        self.root.title("MVC Example - ImageView")
        self.canvas = None  # Canvas widget to display the image.
        self.controls_frame = None  # Frame for control buttons.
        self.open_image_file_button = None  # Button to open a file.
        self.image_label = None  # Label to display the image.
        self.image_path = None  # Path to the image file.
        self.create_widgets()

    # Initialize and place widgets
    def create_widgets(self):

        # Create buttons
        self.label = tk.Label(self.root, text="Enter Image filename:")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.set_img_path_button = tk.Button(self.root, text="Set Image Path")
        self.set_img_path_button.pack()

        self.open_image_file_button = tk.Button(
            self.root, text="Open Image File")
        self.open_image_file_button.pack()

        self.display = tk.Label(self.root, text="")
        self.display.pack()

        self.load_img_button = tk.Button(self.root, text="Load Image")
        self.load_img_button.pack()

        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.pack()

        self.image_canvas = tk.Canvas(
            self.controls_frame, bg="yellow", height=350, width=350, name="image_canvas")
        self.image_canvas.pack()

        # Create a label to display the image once loaded and supplied by the Model
        self.image_label = tk.Label(
            self.image_canvas, text="Image_Label")
        self.image_label.pack()

        self.quit_button = tk.Button(
            self.controls_frame, text="QUIT", fg="red", command=self.root.destroy)
        self.quit_button.pack()

    # def load_image(self, image_path):
    #     # Load image from file
    #     print(f"Image_View.load_image(): Loading image from: {image_path}")
    #     if self.image_path is None:
    #         return
    #     image = ImageTk.PhotoImage(Image.open(image_path))
    #     self.image_label.image = image  # keep a reference so the image doesn't disappear!

    # Display the image
    def display_image(self, image):
        print(f"ImageView.display_image():Displaying image: {image}")
        self.image_label.configure(image=image)
        self.image_label.image = image  # keep a reference so the image doesn't disappear!

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
