# Image Controller Class
# The Controller handles the input from the user, processes it, and updates the
# Model and View.
# It acts as an intermediary between the Model and the View, receiving user
# input and updating the Model and View accordingly.
# The Controller is responsible for managing the data and the rules of the
# application. It notifies the View when the data changes, so the View can
# update itself accordingly.

from PIL import Image, ImageTk


class ImageController:
    """
    Controller class for handling image-related operations and interactions between the model and view.

    Attributes:
        model (ImageModel): The model instance that handles image data and operations.
        view (ImageView): The view instance that handles the user interface.

    Methods:
        bind_events():
            Binds UI events to the corresponding controller methods.
        load_image():
            Handles loading an image from the file system and displaying it in the view.
        save_image():
            Handles saving the current image to the file system.
        crop_image():
            Handles cropping the current image.
        resize_image():
            Handles resizing the current image.
        quit_app():
            Quits the application.
    """

    def __init__(self, model, view):
        self.model = model  # Instance of ImageModel.
        self.view = view  # Instance of ImageView.
        self.bind_events()

    def bind_events(self):
        """
        Binds UI events to the corresponding controller methods.
        """
        self.view.open_image_button.config(command=self.load_image)
        self.view.save_image_button.config(command=self.save_edited_image)
        self.view.crop_image_button.config(command=self.crop_image)
        self.view.resize_image_slider.config(command=self.on_scale_change)
        self.view.rotate_image_left_button.config(
            command=self.rotate_image_left)
        self.view.rotate_image_right_button.config(
            command=self.rotate_image_right)
        self.view.reset_image_button.config(command=self.reset_image)
        self.view.root.bind("<Control-o>", self.handle_key_press)
        self.view.root.bind("<Control-O>", self.handle_key_press)
        self.view.root.bind("<Control-s>", self.handle_key_press)
        self.view.root.bind("<Control-S>", self.handle_key_press)
        self.view.root.bind("<Control-r>", self.handle_key_press)
        self.view.root.bind("<Control-R>", self.handle_key_press)
        self.view.root.bind("<Control-q>", self.handle_key_press)
        self.view.root.bind("<Control-Q>", self.handle_key_press)
        self.view.root.bind("<Left>", self.handle_key_press)
        self.view.root.bind("<Right>", self.handle_key_press)
        self.view.root.bind("<Up>", self.handle_key_press)
        self.view.root.bind("<Down>", self.handle_key_press)
        self.view.root.bind("<c>", self.handle_key_press)
        self.view.root.bind("<C>", self.handle_key_press)
        self.view.quit_button.config(command=self.quit_app)

    def load_image(self):
        """
        Handles loading an image from the file system and displaying it in the view.

        Displays the "Open file" dialog box and loads the selected image from the file system.
        The image is then displayed in the view.

        Returns:
            None
        """
        # Handle loading image
        image_dir = self.model.get_image_dir()
        image_path = self.view.open_image_file(start_path=image_dir)
        self.model.set_image_path(image_path)
        self.model.load_image(image_path)
        image = self.model.get_tk_photoimage()
        self.view.display_image(image)

    def on_scale_change(self, value):
        """
        Handles scaling the current image.

        Sets the scale factor in the model and scales the image.
        The scaled image is then displayed in the view.

        Returns:
            None
        """
        print("Scaling image")
        # print(f"ImageController.on_scale_change(): Scaling image by: {value}")
        # Set a step size for the slider control
        step_size = 1.0
        # Snap to the nearest step
        stepped_value = round(float(value) / step_size) * step_size
        # Convert value returned from the slider control from text value to a float fractional value

        self.view.resize_image_slider_value_label.config(
            text=f"Scale factor: {stepped_value}%"
        )
        scale_value = float(stepped_value)
        # Convert the slider value to a scale factor
        scale_factor = scale_value/100.0
        self.resize_image(scale_factor)

    def save_edited_image(self):
        # Handle saving image
        print("Saving image")
        initial_dir = self.model.get_edited_image_dir()
        initial_file = self.model.get_edited_image_name()
        image_path = self.view.save_edited_image(initial_dir, initial_file)
        self.model.save_edited_image(image_path)

    def reset_image(self):
        # Reset all image edits
        print("Resetting image")
        self.view.set_resize_image_slider_value(100)
        self.model.reset_image()
        image = self.model.get_tk_photoimage()
        self.view.display_image(image)

    def quit_app(self):
        # Quit the application
        print("Quitting application")
        self.view.root.destroy()

    def crop_image(self):
        """
        Handles cropping the current image.

        Sets the crop coordinates in the model and crops the image.
        The cropped image is then displayed in the view.

        Returns:
            None
        """
        print("Cropping image")
        # Handle cropping image
        # Crop coodinates are read from the view
        self.model.crop_image(
            self.view.start_x, self.view.start_y, self.view.end_x, self.view.end_y)
        # Get the cropped image from the model - image in opencv format
        cropped_image = self.model.get_edited_image()
        # Convert the cropped image to tkinter format
        edited_image = self.model.opencv_to_tk(cropped_image)
        # Update the view with the edited image
        self.view.update_edited_image(edited_image)

    def resize_image(self, scale_factor):
        # Handle resizing image
        print("Resizing image")
        # Set the model scale factor
        self.model.set_scale_factor(scale_factor)
        # Get the scaled image as a PhotoImage
        tk_img = self.model.get_edited_scaled_image_as_tk()
        # Update the view with the scaled image
        self.view.update_edited_image(tk_img)

    def set_window_size(self):
        # Handle setting window size
        print("Setting window size")
        pass

    def rotate_image_left(self):
        # Handle rotating image left
        print("Rotating image left")
        # Rotate image counter-clockwise 90 degrees
        self.model.rotate_image(-90)
        tk_img = self.model.get_edited_image_as_tk()
        # Update the view with the edited image
        self.view.update_edited_image(tk_img)

    def rotate_image_right(self):
        # Handle rotating image right
        print("Rotating image right")
        # Rotate image clockwise 90 degrees
        self.model.rotate_image(90)
        tk_img = self.model.get_edited_image_as_tk()
        # Update the view with the edited image
        self.view.update_edited_image(tk_img)
        pass

    def handle_key_press(self, event):
        # Handle key press events
        print(f"ImageController.handle_key_press(): Key pressed: "
              f"char: {event.char}, keycode: ({event.keycode}), "
              f"keysym: {event.keysym}, State: {event.state}")
        # Control key event state = 0x0004
        CONTROL_KEY_STATE = 0x0004
        if event.keysym == "Left":
            self.rotate_image_left()
        if event.keysym == "Right":
            self.rotate_image_right()
        if event.keysym == "Up":
            self.view.increment_resize_image_slider_value()
        if event.keysym == "Down":
            self.view.decrement_resize_image_slider_value()
        if event.keysym.lower() == "o" and event.state & CONTROL_KEY_STATE:
            self.load_image()
        if event.keysym.lower() == "s" and event.state & CONTROL_KEY_STATE:
            self.save_edited_image()
        if event.keysym == "c" or event.keysym == "C":
            self.crop_image()
        if event.keysym.lower() == "r" and event.state & CONTROL_KEY_STATE:
            self.reset_image()
        if event.keysym.lower() == "q" and event.state & CONTROL_KEY_STATE:
            self.quit_app()
