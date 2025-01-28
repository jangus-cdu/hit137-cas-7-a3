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
    """
    A class to represent the main window for image viewing and editing using Tkinter.

    Attributes
    ----------
    root : Tk
        The main Tkinter window.
    main_window_width : int
        Width of the main window.
    main_window_height : int
        Height of the main window.
    menu_frame : Frame
        Frame for the menu.
    controls_frame : Frame
        Frame for control buttons.
    image_frame_original : Frame
        Frame for the original image.
    image_frame_edited : Frame
        Frame for the edited image.
    bottom_frame : Frame
        Bottom frame for displaying various info.
    open_image_button : Button
        Button to open a file.
    save_image_button : Button
        Button to save the image.
    crop_image_button : Button
        Button to crop the image.
    rotate_image_button : Button
        Button to rotate the image.
    quit_button : Button
        Button to quit the application.
    image_original_title : Label
        Label indicating the original image frame.
    image_original_label : Label
        Label holding the original image.
    image_edited_title : Label
        Label indicating the edited image frame.
    image_edited_label : Label
        Label holding the edited image.
    image_path : str
        Path to the image file.
    bottom_label_0 : Label
        Status bar label 0.
    bottom_label_1 : Label
        Status bar label 1.
    bottom_label_2 : Label
        Status bar label 2.
    bottom_label_3 : Label
        Status bar label 3.
    bottom_label_4 : Label
        Status bar label 4.
    bottom_label_5 : Label
        Status bar label 5.

    Methods
    -------
    create_widgets():
        Initializes and places widgets in the main window.
    display_image(image):
        Displays the given image in the original image frame.
    open_image_file(start_path="/") -> str:
        Opens a file dialog to select an image file and returns the file path.
    update_edited_image(image):
        Updates the edited image frame with the given image.
    update_image(image):
        Updates the displayed image.
    show_message(message):
        Displays a message to the user.
    get_input():
        Gets user input from the entry widget.
    set_display(text):
        Sets the display text.
    """

    def __init__(self, root):
        self.root = root  # The main Tkinter window.
        self.root.title("Main Window - ImageView")
        self.main_window_width = 800  # Width of the main window.
        self.main_window_height = 600  # Height of the main window.

        # Main Window Frames
        self.controls_frame = None  # Frame for control buttons.
        self.image_frame_orignal = None  # Frame for the original image.
        self.image_frame_edited = None  # Frame for the deited image.
        self.bottom_frame = None  # Bottom Frame for displaying various info.

        # Image Edit Canvas
        self.image_canvas_original = None  # Canvas for editing the image.
        self.start_x = None
        self.start_y = None
        self.rect = None

        # Buttons
        self.open_image_button = None  # Button to open a file.
        self.save_image_button = None  # Button to save the image.
        self.crop_image_button = None  # Button to crop the image.
        self.rotate_image_button = None  # Button to rotate the image.
        self.quit_button = None  # Button to quit the application.

        # Image View Labels
        self.image_original_title = None  # Indicates Original Image Frame
        self.image_original_label = None  # Holds Original image.

        # Image Edit Labels
        self.image_edited_title = None  # Indicates Edited Image Frame
        self.image_edited_label = None  # Holds Edited image.
        self.image_path = None  # Path to the image file.
        # Status bar labels
        self.bottom_label_0 = None
        self.bottom_label_1 = None
        self.bottom_label_2 = None
        self.bottom_label_3 = None
        self.bottom_label_4 = None
        self.bottom_label_5 = None

        # Call create widgets method
        self.create_widgets()

    # Initialize and place widgets
    def create_widgets(self):
        # Setup the Main window
        self.root.config(width=self.main_window_width,
                         height=self.main_window_height, bg="skyblue")

        self.root.minsize(self.main_window_width/2,
                          self.main_window_height/2)  # Minimum window size
        # self.root.iconbitmap('./assets/app.ico') # Set a custom app icon
        # self.root.attributes('-topmost', 10) # Place window on top of all others
        # tkinter columconfigure and rowconfigure
        # https://stackoverflow.com/questions/21893288/tkinter-columconfigure-and-rowconfigure
        # Set frame priorities for resizing
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(4, weight=1)

        # Create main frames - using grid layout for frame and widget placement
        self.controls_frame = tk.Frame(
            self.root, width=200, height=400, bg="orange")
        self.image_frame_original = tk.Frame(
            self.root, width=400, height=400, bg="cyan")
        self.image_frame_edited = tk.Frame(
            self.root, width=400, height=400, bg="blue")
        self.bottom_frame = tk.Frame(
            self.root, width=800, height=10, bg="green")

        # Layout main Frames
        self.controls_frame.grid(row=0, column=0, columnspan=1, sticky="nsew")
        self.image_frame_original.grid(
            row=0, column=1, columnspan=3,  sticky="nsew")
        self.image_frame_edited.grid(
            row=0, column=4,  columnspan=3, sticky="nsew")
        self.bottom_frame.grid(row=1, column=0, columnspan=7, sticky="ew")

        # Create buttons
        self.open_image_button = tk.Button(
            self.controls_frame, text="Open Image")
        self.save_image_button = tk.Button(
            self.controls_frame, text="Save Image")
        self.crop_image_button = tk.Button(
            self.controls_frame, text="Crop Image")
        self.rotate_image_button = tk.Button(
            self.controls_frame, text="Rotate Image")
        self.quit_button = tk.Button(
            self.controls_frame, text="QUIT", fg="red")

        # Layout Control Frame Widgets
        self.open_image_button.grid(row=0)
        self.save_image_button.grid(row=1)
        self.crop_image_button.grid(row=2)
        self.rotate_image_button.grid(row=3)
        self.quit_button.grid(row=4)

        # Create Image Frame Widgets
        self.image_original_title = tk.Label(
            self.image_frame_original, text="Original Image")
        self.image_canvas_original = tk.Canvas(
            self.image_frame_original, cursor="cross", height=0, width=0)
        # self.image_canvas_original.bind("<ButtonPress-1>", self.on_mouse_press)
        # self.image_canvas_original.bind("<B1-Motion>", self.on_mouse_drag)
        # self.image_canvas_original.bind(
        #     "<ButtonRelease-1>", self.on_mouse_release)
        # self.image_label_original = tk.Label(
        # self.image_frame_original, text="Image_Label_Original")

        self.image_edited_title = tk.Label(
            self.image_frame_edited, text="Edited Image")
        self.image_label_edited = tk.Label(
            self.image_frame_edited, text="Image_Label_Edited")

        # Layout Image Frame Widgets
        self.image_original_title.grid(row=0, sticky="w")
        self.image_canvas_original.grid(row=1, sticky="nsew")
        # self.image_label_original.grid(row=1)
        self.image_edited_title.grid(row=0, sticky="w")
        self.image_label_edited.grid(row=1, sticky="nsew")

        # Create Bottom Frame Widgets
        self.bottom_label_0 = tk.Label(
            self.bottom_frame, text="Bottom Label 0")
        self.bottom_label_1 = tk.Label(
            self.bottom_frame, text="Bottom Label 1")
        self.bottom_label_2 = tk.Label(
            self.bottom_frame, text="Bottom Label 2")
        self.bottom_label_3 = tk.Label(
            self.bottom_frame, text="Bottom Label 3")
        self.bottom_label_4 = tk.Label(
            self.bottom_frame, text="Bottom Label 4")
        self.bottom_label_5 = tk.Label(
            self.bottom_frame, text="Bottom Label 5")

        # Layout Bottom Frame Widgets
        self.bottom_label_0.grid(row=0, column=0, columnspan=1, sticky="ew")
        self.bottom_label_1.grid(row=0, column=1, columnspan=1, sticky="ew")
        self.bottom_label_2.grid(row=0, column=2, columnspan=1, sticky="ew")
        self.bottom_label_3.grid(row=1, column=0, columnspan=1, sticky="ew")
        self.bottom_label_4.grid(row=1, column=1, columnspan=1, sticky="ew")
        self.bottom_label_5.grid(row=1, column=2, columnspan=1, sticky="ew")

    # Open a file dialog to select an image file
    def open_image_file(self, start_path="/") -> str:
        print("ImageView.open_image_file(): Opening file dialog...")
        print(f"ImageView.open_image_file(): Start path: {start_path}")
        file_path = filedialog.askopenfilename(
            initialdir=start_path, title="Select file", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
        print(f"Image_View.open_file(): Selected file: {file_path}")
        return file_path

    # Display the image
    def display_image(self, image):
        print(f"ImageView.display_image():Displaying image: {image}")
        print(f"image.width(): {image.width()
                                }, image.height(): {image.height()}")
        # Resize the window to fit the image
        self.image_frame_original.config(width=image.width(),
                                         height=image.height())
        if image.width() > self.root.winfo_width()/2:
            self.root.config(width=image.width())
        if image.height() > self.root.winfo_height():
            self.root.config(height=image.height())

        # Reset the canvas and display the image
        self.image_canvas_original.delete("all")
        self.image_canvas_original.config(width=image.width(),
                                          height=image.height())
        self.image_canvas_original.create_image(
            0, 0, anchor=tk.NW, image=image)
        # Now update the edited image to display the same image
        self.update_edited_image(image)

    # def on_mouse_press(self, event):
    #     self.start_x = event.x
    #     self.start_y = event.y
    #     if self.rect:
    #         self.image_canvas_original.delete(self.rect)
    #     self.rect = self.image_canvas_original.create_rectangle(
    #         self.start_x, self.start_y, self.start_x, self.start_y, outline="red")

    # def on_mouse_drag(self, event):
    #     if self.rect:
    #         self.image_canvas_original.coords(
    #             self.rect, self.start_x, self.start_y, event.x, event.y)

    # def on_mouse_release(self, event):
    #     if self.rect:
    #         self.ImageController.handle_crop(
    #             self.start_x, self.start_y, event.x, event.y)

    def update_edited_image(self, image):
        print(
            f"ImageView.update_edited_image(): Updating edited image: {image}")
        self.image_frame_edited.config(width=image.width(),
                                       height=image.height())
        self.image_label_edited.configure(image=image)
        self.image_label_edited.image = image

    def update_image(self, image):
        # Update displayed image
        pass
