import tkinter as tk
from PIL import Image, ImageTk


class ImageView:

    def __init__(self, root):
        self.root = root  # The main Tkinter window.
        self.root.title("MVC Example - ImageView")
        self.canvas = None  # Canvas widget to display the image.
        self.controls_frame = None  # Frame for control buttons.
        self.image_label = None  # Label to display the image.
        self.create_widgets()

    def create_widgets(self):
        # Initialize and place widgets
        # self.canvas = tk.Canvas(self.root, width=500, height=500)
        # self.canvas.pack()

        # Create buttons
        self.label = tk.Label(self.root, text="Enter Image filename:")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Submit")
        self.button.pack()

        self.display = tk.Label(self.root, text="")
        self.display.pack()

        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.pack()

        self.image_canvas = tk.Canvas(
            self.controls_frame, bg="yellow", height=350, width=350, name="image_canvas")
        self.image_canvas.pack()

        # Load the image file
        image_path = "test-image-small.jpeg"
        image = Image.open(image_path)
        # Define the new size
        # new_size = (50, 50)  # Width, Height
        # resize_image = image.resize(new_size)
        photo = ImageTk.PhotoImage(image)

        print(f"photo: height: {photo.height()} x width: {photo.width()}")

        # Create a label to display the image
        self.image_label = tk.Label(
            self.image_canvas, text="Test-Image", image=photo)
        self.image_label.image = photo  # keep a reference so the image doesn't disappear!
        self.image_label.pack()

        self.quit_button = tk.Button(
            self.controls_frame, text="QUIT", fg="red", command=self.root.destroy)
        self.quit_button.pack()

    def update_image(self, image):
        # Update displayed image
        pass

    def show_message(self, message):
        # Display message to user
        pass

    def get_input(self):
        return self.entry.get()

    def set_display(self, text):
        self.display.config(text=text)
