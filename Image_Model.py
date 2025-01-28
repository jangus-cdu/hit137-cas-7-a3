# Image Model Class
# The Model represents the data and the business logic of the application.
# It is responsible for managing the data and the rules of the application.
# The Model is independent of the user interface and the user input.
# It notifies the View (via the Controller) when the data changes, so the View
# can update itself accordingly.

import os
from PIL import Image, ImageTk


class ImageModel:
    """
    A class to represent an image model.

    Attributes
    ----------
    image_path : str
        Path to the image file.
    image_dir : str
        Directory of the image file.
    image : ImageTk.PhotoImage
        The image object.
    original_image : ImageTk.PhotoImage
        The original image object.
    edited_image : ImageTk.PhotoImage
        The edited image object.

    Methods
    -------
    set_image_path(path):
        Sets the path to the image file.
    get_image_path():
        Gets the path to the image file.
    get_image_dir():
        Gets the directory of the image file.
    load_image(image_path) -> ImageTk.PhotoImage:
        Loads an image from the given path.
    get_image():
        Returns the image object.
    save_image(path):
        Saves the edited image to the given path.
    crop_image(x, y, width, height):
        Crops the image.
        Returns the cropped image.
    apply_filter(filter_type):
        Applies a filter to the image.
    resize_image(width, height):
        Resizes the image.
    rotate_image(angle):
        Rotates the image.
    """

    def __init__(self):
        self.image_path = None  # Path to the image file.
        self.image_dir = "/"  # Directory of the image file - default is root.
        self.image = None  # The image object.
        self.original_image = None  # The original image object.
        self.edited_image = None  # The edited image object.

    # Sets the path to the image file.
    def set_image_path(self, path):
        print(f"ImageModel.set_image_path(): Setting image path to: {path}")
        self.image_path = path
        self.image_dir = os.path.dirname(self.image_path)

    # Gets the path to the image file.
    def get_image_path(self):
        print(f"ImageModel.get_image_path(): Returning image path: {
              self.image_path}")
        return self.image_path

    # Gets the directory of the image file.
    def get_image_dir(self):
        print(f"ImageModel.get_image_dir(): Returning image directory: {
              self.image_dir}")
        return self.image_dir

    # Loads an image from the given path.
    def load_image(self, image_path) -> ImageTk.PhotoImage:
        # Load image logic
        print(f"ImageModel.load_image(): Loading image from: {image_path}")
        self.image = ImageTk.PhotoImage(Image.open(self.image_path))
        return self.image

    # Returns the image object.
    def get_image(self):
        print(f"ImageModel.get_photo(): Returning photo: {self.image}")
        return self.image

    # Saves the edited image to the given path.
    def save_image(self, path):
        # Save image logic
        pass

    # Crops the image.
    def crop_image(self, x, y, width, height) -> ImageTk.PhotoImage:
        # Crop image logic
        pass

    # Resizes the image.
    def resize_image(self, width, height):
        # Resize image logic
        pass

    # Rotates the image.
    def rotate_image(self, angle):
        # Rotate image logic
        pass
