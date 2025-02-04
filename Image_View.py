# Image View Class
# The View class is responsible for displaying the user interface and handling
# user input. It interacts with the Model and Controller to display data and
# receive user input. The View class is implemented using the Tkinter library.
# The View class contains methods to create and manage the user interface,
# load and display images, and handle user input. The View will update with
# changes to the Model and Controller.

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageView:
    """
    A class to represent the main window for image viewing and editing using Tkinter.

    Attributes
    root : Tk
        The main Tkinter window.
    main_window_width : int
        Width of the main window.
    main_window_height : int
        Height of the main window.
    controls_frame : Frame
        Frame for control buttons.
    image_frame_original : Canvas
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
    resize_image_slider : Scale
        Slider to resize the edited image.
    rotate_image_button : Button
        Button to rotate the image.
    quit_button : Button
        Button to quit the application.
    image_original_title : Label
        Label indicating the original image frame.
    image_canvas_original : Canvas
        Canvas for displaying and editing the original image.
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
    bind_mouse_events():
        Binds mouse events to the image editing canvas.
    """

    def __init__(self, root):
        self.root = root  # The main Tkinter window.
        self.root.title("Main Window - ImageView")
        self.main_window_width = 800  # Width of the main window.
        self.main_window_height = 600  # Height of the main window.

        # Main Window Frames
        self.content_frame = None
        self.controls_frame = None  # Frame for control buttons.
        self.image_frame_orignal = None  # Frame for the original image.
        self.image_frame_edited = None  # Frame for the deited image.
        self.bottom_frame = None  # Bottom Frame for displaying various info.

        # Image Edit Canvas
        self.image_canvas_original = None  # Canvas for editing the image.
        self.start_x = None  # Start x coordinate on mouse click
        self.start_y = None  # Start y coordinate on mouse click
        self.end_x = None  # End x coordinate on mouse release
        self.end_y = None  # End y coordinate on mouse release
        self.rect = None

        # Control Frame Buttons
        self.open_image_button = None  # Button to open a file.
        self.save_image_button = None  # Button to save the image.
        self.crop_image_button = None  # Button to crop the image.
        self.rotate_image_left_button = None  # Button to rotate the image.
        self.rotate_image_right_button = None  # Button to rotate the image.
        self.quit_button = None  # Button to quit the application.

        # Control Frame Labels
        self.KEYBOARD_SHORTCUTS_TEXT = f"Keyboard Shortcuts:\n" \
            f"Control-O: Open\n" \
            f"Control-S: Save\n" \
            f"Control-Q: Quit\n" \
            f"Left Arrow: Rotate Left\n" \
            f"Right Arrow: Rotate Right\n" \
            f"Up Arrow: Expand Image Size\n" \
            f"Down Arrow: Shrink Image Size\n" \
            f"C: Crop Image\n"
        self.kbd_shortcuts_label = None

        # Button Icons
        self.icon_rotate_left = None
        self.icon_rotate_right = None
        self.icon_rotate_left_path = "icons/rotate-left-24.png"
        self.icon_rotate_right_path = "icons/rotate-right-24.png"

        # Sliders
        self.resize_image_label = None  # Label for the resize slider.
        self.resize_image_slider = None  # Slider to resize the edited image.

        # Image View Labels
        self.image_original_title = None  # Indicates Original Image Frame
        self.image_path = None  # Path to the image file.

        # Image Edit Labels
        self.image_edited_title = None  # Indicates Edited Image Frame
        self.image_edited_label = None  # Holds Edited image.

        # Status bar labels
        self.bottom_label_0 = None
        self.bottom_label_1 = None
        self.bottom_label_2 = None
        self.bottom_label_3 = None
        self.bottom_label_4 = None
        self.bottom_label_5 = None

        # Load Button Icons
        self.load_icons()

        # Call create widgets method
        self.create_widgets()

        # Bind UI mouse events to methods
        self.bind_mouse_events()

    def create_widgets(self):
        """
        Initializes and places all the widgets in the main window.
        """
        self.root.config(width=self.main_window_width,
                         height=self.main_window_height, bg="skyblue")

        self.root.minsize(int(self.main_window_width/2),
                          # Minimum window size
                          int(self.main_window_height/2))
        # self.root.iconbitmap('./assets/app.ico') # Set a custom app icon
        # self.root.attributes('-topmost', 1) # Place window on top of all others
        # tkinter columconfigure and rowconfigure
        # https://stackoverflow.com/questions/21893288/tkinter-columconfigure-and-rowconfigure
        self.content_frame = ttk.Frame(self.root, padding=(3, 3, 12, 12))

        # Create main frames - using grid layout for frame and widget placement
        self.controls_frame = ttk.Frame(
            self.content_frame, width=200, height=400, borderwidth=3, relief="ridge", padding=(3, 3, 6, 6))
        self.image_frame_original = ttk.Frame(
            self.content_frame, width=400, height=400, borderwidth=3, relief="ridge")
        self.image_frame_edited = ttk.Frame(
            self.content_frame, width=400, height=400, borderwidth=3, relief="ridge")
        self.bottom_frame = ttk.Frame(
            self.content_frame, width=1000, height=10, borderwidth=3, relief="ridge")

        # Layout main Frames
        self.content_frame.grid(column=0, row=0, columnspan=7, sticky="nsew")
        self.controls_frame.grid(row=0, column=0, columnspan=1, sticky="nsew")
        self.image_frame_original.grid(
            row=0, column=1, columnspan=3,  sticky="nsew")
        self.image_frame_edited.grid(
            row=0, column=4,  columnspan=3, sticky="nsew")
        self.bottom_frame.grid(row=1, column=0, columnspan=7, sticky="ew")

        # Create buttons
        self.open_image_button = ttk.Button(
            self.controls_frame, text="Open Image")
        self.save_image_button = ttk.Button(
            self.controls_frame, text="Save Image")
        self.crop_image_button = ttk.Button(
            self.controls_frame, text="Crop Image")
        if self.icon_rotate_left == None:
            button_text = "Rotate Image Left"
        else:
            button_text = ""
        self.rotate_image_left_button = tk.Button(
            self.controls_frame, image=self.icon_rotate_left, text=button_text)
        if self.icon_rotate_right == None:
            button_text = "Rotate Image Right"
        else:
            button_text = ""
        self.rotate_image_right_button = tk.Button(
            self.controls_frame, image=self.icon_rotate_right, text=button_text)
        self.quit_style = ttk.Style()
        self.quit_style.configure('Quit.TButton', foreground='red')
        self.quit_button = ttk.Button(
            self.controls_frame, text="QUIT", style='Quit.TButton')
        self.kbd_shortcuts_label = ttk.Label(
            self.controls_frame, text=self.KEYBOARD_SHORTCUTS_TEXT
        )
        # Create Sliders
        self.resize_image_label = ttk.Label(
            self.controls_frame, text="Resize Image")
        self.resize_image_slider = ttk.Scale(
            self.controls_frame, from_=0, to=100, orient="horizontal")

        # Layout Control Frame Widgets
        self.open_image_button.grid(
            row=0, column=0, columnspan=2, sticky="nsew")
        self.save_image_button.grid(
            row=1, column=0, columnspan=2, sticky="nsew")
        self.crop_image_button.grid(
            row=2, column=0, columnspan=2, sticky="nsew")
        self.resize_image_label.grid(
            row=3, column=0, columnspan=2, sticky="nsew")
        self.resize_image_slider.grid(
            row=4, column=0, columnspan=2, sticky="nsew")
        self.rotate_image_left_button.grid(
            row=5, column=0, rowspan=2, sticky="nsew", ipadx=3, ipady=3)
        self.rotate_image_right_button.grid(
            row=5, column=1,  rowspan=2, sticky="nsew", ipadx=3, ipady=3)
        self.quit_button.grid(row=7, column=0, columnspan=2, sticky="nsew")
        self.kbd_shortcuts_label.grid(
            row=8, column=0, columnspan=2, sticky="nsew")

        # Create Image Frame Widgets
        self.image_original_title = ttk.Label(
            self.image_frame_original, text="Original Image")
        self.image_canvas_original = tk.Canvas(
            self.image_frame_original, bg="white", cursor="cross", height=0, width=0)

        self.image_edited_title = ttk.Label(
            self.image_frame_edited, text="Edited Image")
        self.image_label_edited = ttk.Label(
            self.image_frame_edited)

        # Layout Image Frame Widgets
        self.image_original_title.grid(row=0, sticky="w")
        self.image_canvas_original.grid(row=1, sticky="nsew")
        self.image_edited_title.grid(row=0, sticky="w")
        # self.image_label_edited.grid(row=1, sticky="nsew")
        self.image_label_edited.grid(row=1)

        # Create Bottom Frame Widgets
        self.bottom_label_0 = ttk.Label(
            self.bottom_frame, text="Bottom Label 0")
        self.bottom_label_1 = ttk.Label(
            self.bottom_frame, text="Bottom Label 1")
        self.bottom_label_2 = ttk.Label(
            self.bottom_frame, text="Bottom Label 2")
        self.bottom_label_3 = tk.Label(
            self.bottom_frame, text="Bottom Label 3")
        self.bottom_label_4 = tk.Label(
            self.bottom_frame, text="Bottom Label 4")
        self.bottom_label_5 = tk.Label(
            self.bottom_frame, text="Bottom Label 5")

        # Layout Bottom Frame Widgets
        self.bottom_label_0.grid(row=0, column=0, sticky="w")
        self.bottom_label_1.grid(row=0, column=1)
        self.bottom_label_2.grid(row=0, column=4)
        self.bottom_label_3.grid(row=1, column=0, sticky="w")
        self.bottom_label_4.grid(row=1, column=1)
        self.bottom_label_5.grid(row=1, column=4)

        # Set resizing priorities
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.content_frame.columnconfigure(0, weight=0)
        self.content_frame.columnconfigure(1, weight=1)
        self.content_frame.columnconfigure(4, weight=1)
        self.content_frame.rowconfigure(0, weight=1)
        self.content_frame.rowconfigure(1, weight=0)
        self.content_frame.rowconfigure(2, weight=0)

        # self.controls_frame.columnconfigure(0, weight=1)
        # self.controls_frame.rowconfigure(5, weight=1)

        self.bottom_frame.columnconfigure(0, weight=0)
        self.bottom_frame.columnconfigure(1, weight=1)
        self.bottom_frame.columnconfigure(4, weight=1)

    # Open a file dialog to select an image file

    def open_image_file(self, start_path="/") -> str:
        """
        Opens a file dialog to select an image file and returns the file path.

        Parameters
        start_path (str): The initial directory path for the file dialog.

        Returns
        str: The file path of the selected image.
        """
        print("ImageView.open_image_file(): Opening file dialog...")
        print(f"ImageView.open_image_file(): Start path: {start_path}")
        file_path = filedialog.askopenfilename(
            initialdir=start_path, title="Select file", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
        print(f"Image_View.open_file(): Selected file: {file_path}")
        return file_path

        print("ImageView.open_image_file(): Opening file dialog...")
        print(f"ImageView.open_image_file(): Start path: {start_path}")
        file_path = filedialog.askopenfilename(
            initialdir=start_path, title="Select file", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))
        print(f"Image_View.open_file(): Selected file: {file_path}")
        return file_path

    def display_image(self, image):
        """
        Displays the image in the original image frame.
        Also resizes the window to fit the image and updates the edited image.

        Parameters
        image (ImageTk.PhotoImage): The image to be displayed.

        Returns
        None
        """
        print(f"ImageView.display_image():Displaying image: {image}")
        print(f"image.width(): {image.width()}, "
              f"image.height(): {image.height()}")
        # Resize the window to fit the image
        self.content_frame.config(width=self.main_window_width,
                                  height=self.main_window_height)
        self.image_frame_original.config(width=image.width(),
                                         height=image.height())

        # Reset the canvas and display the image
        self.image_canvas_original.delete("all")
        self.image_canvas_original.config(width=image.width(),
                                          height=image.height())
        self.image_canvas_original.create_image(
            0, 0, anchor=tk.NW, image=image)
        self.image_canvas_original.image = image

        # Now update the edited image to display the same image
        self.update_edited_image(image)

    def bind_mouse_events(self):
        """
        Binds mouse events to the canvas for image editing.

        This method sets up event listeners for mouse actions on the original image canvas.
        It captures mouse press, drag, and release events to enable image cropping.
        """

        # Canvas mouse events
        self.image_canvas_original.bind("<ButtonPress-1>", self.on_mouse_press)
        self.image_canvas_original.bind("<B1-Motion>", self.on_mouse_drag)
        self.image_canvas_original.bind(
            "<ButtonRelease-1>", self.on_mouse_release)

    def on_mouse_press(self, event):
        """
        Handles the mouse press event for the original image canvas.

        When the user clicks on the original image canvas, this method is called.
        It captures the mouse coordinates and marks the start of the selection area.
        The selection area is shown as a red rectangle on the canvas.
        """
        print(f"ImageView.on_mouse_press(): Mouse clicked at: "
              f"{event.x}, {event.y}")
        self.start_x = event.x
        self.start_y = event.y
        if self.rect:
            self.image_canvas_original.delete(self.rect)
        self.rect = self.image_canvas_original.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y, outline="red")

    # Handle mouse drag event
    def on_mouse_drag(self, event):
        """
        Handles the mouse drag event for the original image canvas.

        When the user drags the mouse on the original image canvas, this method is called.
        It updates the coordinates of the selection rectangle to show the current drag position.
        """
        if self.rect:
            self.image_canvas_original.coords(
                self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_mouse_release(self, event):
        """
        Handles the mouse release event for the original image canvas.

        When the user releases the mouse button on the original image canvas, this method is called.
        It captures the final mouse coordinates and sets the end of the selection area.
        This method is used to finalize the cropping rectangle.

        Parameters
        event (tk.Event):
            The event object containing the mouse release coordinates.

        Returns
        None
        """

        print(f"ImageView.on_mouse_release(): Mouse released at: "
              f"{event.x}, {event.y}")
        self.end_x = event.x
        self.end_y = event.y

    def update_edited_image(self, image):
        """
        Updates the edited image in the edited image frame.

        This method is called when the edited image needs to be updated, such as when the user
        selects a new image from the file system or when the controller updates the edited image.

        Parameters
        image (ImageTk.PhotoImage):
            The image to be displayed in the edited image frame.

        Returns
        None
        """
        # print(
        # f"ImageView.update_edited_image(): Updating edited image: {image}")
        print(f"ImageView.update_edited_image():Displaying image: {image}")
        print(f"image.width(): {image.width()}, "
              f"image.height(): {image.height()}")
        self.image_frame_edited.config(width=image.width(),
                                       height=image.height())
        self.image_label_edited.configure(image=image)
        self.image_label_edited.image = image

    def update_image(self, image):
        # Update displayed image
        pass

    def load_icons(self):
        # Load icons
        print(f"ImageView.load_icons(): Loading icons...")
        # Load images using Pillow
        try:
            image = Image.open(self.icon_rotate_left_path)
            self.icon_rotate_left = ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.icon_rotate_left = None
        try:
            image = Image.open(self.icon_rotate_right_path)
            self.icon_rotate_right = ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.icon_rotate_right = None
