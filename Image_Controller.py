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
        self.view.save_image_button.config(command=self.save_image)
        self.view.crop_image_button.config(command=self.crop_image)
        self.view.rotate_image_left_button.config(
            command=self.rotate_image_left)
        self.view.rotate_image_right_button.config(
            command=self.rotate_image_right)
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
        # image = self.model.get_image()
        image = self.model.get_tk_photoimage()
        self.view.display_image(image)

    def save_image(self):
        # Handle saving image
        print("Saving image")
        pass

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
        self.model.set_crop_coords(
            self.view.start_x, self.view.start_y, self.view.end_x, self.view.end_y)
        cropped_image = self.model.get_cropped_image()
        if cropped_image:
            self.view.update_edited_image(cropped_image)

    def resize_image(self):
        # Handle resizing image
        print("Resizing image")
        pass

    def set_window_size(self):
        # Handle setting window size
        print("Setting window size")
        pass

    def rotate_image_left(self):
        # Handle rotating image left
        print("Rotating image left")
        # Rotate image anti-clockwise 90 degrees
        # current_angle = self.model.get_rotation_angle()
        # if current_angle - 90 < -360:
        #     new_angle = current_angle - 90 + 360
        # elif current_angle - 90 == -360:
        #     new_angle = 0
        # else:
        #     new_angle = current_angle - 90
        # self.model.set_rotation_angle(new_angle)
        # self.model.set_rotation_angle(-90)
        # Get the rotated image from the model - image in opencv format
        self.model.rotate_image(-90)
        tk_img = self.model.get_edited_image_as_tk()

        # Convert edited_image in opencv format to pil image
        # pil_img = self.model.opencv_to_pil(edit_image)
        # Convert the rotated image to tkinter photo format
        # tk_img = ImageTk.PhotoImage(pil_img)

        # tk_img = self.model.opencv_to_tk(edit_image)
        # Update the view with the edited image
        self.view.update_edited_image(tk_img)

    def rotate_image_right(self):
        # Handle rotating image right
        print("Rotating image right")
        # Rotate image clockwise 90 degrees
        # current_angle = self.model.get_rotation_angle()
        # if current_angle + 90 > 360:
        #     new_angle = current_angle + 90 - 360
        # elif current_angle + 90 == 360:
        #     new_angle = 0
        # else:
        #     new_angle = current_angle + 90
        # self.model.set_rotation_angle(new_angle)
        # Get the rotated image from the model - image in opencv format
        # rotated_image = self.model.get_edited_image()
        # Convert the rotated image to tkinter photo format
        # tk_img = self.model.opencv_to_tk(rotated_image)
        self.model.rotate_image(90)
        tk_img = self.model.get_edited_image_as_tk()
        # Update the view with the edited image
        self.view.update_edited_image(tk_img)
        pass
