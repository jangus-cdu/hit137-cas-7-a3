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
    image_path (str): 
        Path to the image file.
    image_dir (str): 
        Directory of the image file.
    image (ImageTk.PhotoImage): 
        The image object.
    original_image (ImageTk.PhotoImage):
        The original image object.
    edited_image (ImageTk.PhotoImage):
        The edited image object.

    Methods
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
        self.crop_coords = None  # Coordinates for cropping the image.

    def set_image_path(self, path):
        """
        Sets the path to the image file and updates the image directory.

        Parameters
        path (str): The path to the image file.

        Returns
        None
        """
        print(f"ImageModel.set_image_path(): Setting image path to: {path}")
        self.image_path = path
        self.image_dir = os.path.dirname(self.image_path)

    def get_image_path(self):
        """
        Gets the path to the image file.

        Returns
        str: The path to the image file.
        """
        print(f"ImageModel.get_image_path(): Returning image path: "
              f"{self.image_path}")
        return self.image_path

    def get_image_dir(self):
        """
        Gets the directory of the image file.

        Returns
        str: The directory of the image file.
        """
        print(f"ImageModel.get_image_dir(): Returning image directory: "
              f"{self.image_dir}")
        return self.image_dir

    def load_image(self, image_path):
        """
        Loads an image from the given path.

        Parameters
        image_path (str): The path to the image file.

        Returns
        ImageTk.PhotoImage: The loaded image object.
        """
        # Load image logic
        print(f"ImageModel.load_image(): Loading image from: {image_path}")
        self.image = ImageTk.PhotoImage(Image.open(self.image_path))

    def get_image(self):
        """
        Gets the loaded image object.

        Returns
        ImageTk.PhotoImage: The loaded image object.
        """
        print(f"ImageModel.get_photo(): Returning image: {self.image}")
        return self.image

    # Saves the edited image to the given path.
    def save_image(self, path):
        # Save image logic
        pass

    def set_crop_coords(self, start_x, start_y, end_x, end_y):
        """
        Sets the coordinates for cropping the image.

        Parameters
        start_x (int): The starting x-coordinate of the cropping rectangle.
        start_y (int): The starting y-coordinate of the cropping rectangle.
        end_x (int): The ending x-coordinate of the cropping rectangle.
        end_y (int): The ending y-coordinate of the cropping rectangle.

        Returns
        None
        """
        self.crop_coords = (start_x, start_y, end_x, end_y)

    def get_cropped_image(self) -> ImageTk.PhotoImage:
        """
        Gets the cropped image object.

        Returns
        ImageTk.PhotoImage: The cropped image object or None if no image is loaded.
        """
        if self.image and self.crop_coords:
            # Convert to PIL.Image to access crop() method
            img = ImageTk.getimage(self.image)
            return ImageTk.PhotoImage(img.crop(self.crop_coords))
        return None

    # Crops the image.
    def crop_image(self, x, y, width, height) -> ImageTk.PhotoImage:
        # Crop image logic
        pass

    # Resizes the image.
    def resize_image(self, width, height):
        # Resize image logic
        pass
