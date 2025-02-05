# Image Model Class
# The Model represents the data and the business logic of the application.
# It is responsible for managing the data and the rules of the application.
# The Model is independent of the user interface and the user input.
# It notifies the View (via the Controller) when the data changes, so the View
# can update itself accordingly.

import os
import cv2  # OpenCV library
import numpy as np
from PIL import Image, ImageTk


class ImageModel:
    """
    A class to represent an image model.

    Attributes
    image_path (str): 
        Path to the image file.
    image_dir (str): 
        Directory of the image file.
    image (OpenCV image): 
        The image object loaded from a file.
    original_image (OpenCV image):
        The original image object.
    edited_image (OpenCV image):
        The edited image object.
    edited_image_dir (str): 
        Directory of the edited image file.
    edited_image_path (str): 
        Path to the edited image file.
    edited_image_name (str): 
        Save the name of the edited image.
    crop_coords (tuple): 
        Coordinates for cropping the image.
    rotation_angle (int): 
        Angle for rotating the image.
    scale_factor (float): 
        Factor for scaling the image

    Methods
    __init__():
        Initializes the ImageModel object.
    set_image_path(path):
        Sets the path to the image file.
    get_image_path():
        Gets the path to the image file.
    get_image_dir():
        Gets the directory of the image file.
    load_image(image_path):
        Loads an image from the given path using OpenCV.
    get_image():
        Returns the image object.
    get_tk_photoimage():
        Returns the image as a tkinter photoimage object.
    opencv_to_pil(self, image):
        Converts an OpenCV image to a PIL image.
    opencv_to_tk(self, image):
        Converts an OpenCV image to a tkinter photoimage object.
    is_opencv_image(self, image):
        Checks if the given image is an OpenCV image.
    save_image(path):
        Saves the edited image to the given path.
    crop_image(x, y, width, height):
        Crops the image.
        Returns the cropped image.
    rotate_image(angle):
        Rotates the image.
    """

    def __init__(self):
        self.image_path = None  # Path to the image file.
        self.image_dir = "/"  # Directory of the image file - default is root.
        self.image = None  # The image object - an OpenCV image.
        self.original_image = None  # The original image object.
        self.edited_image = None  # The edited image object.
        self.edited_image_dir = self.image_dir  # Edited image directory.
        self.edited_image_path = None  # Path to the edited image file.
        self.edited_image_name = None  # Save the name of the edited image.
        self.crop_coords = None  # Coordinates for cropping the image.
        self.rotation_angle = 0  # Angle for rotating the image.
        self.scale_factor = 1.0  # Factor for scaling the image

    def get_image_path(self):
        """
        Gets the path to the image file.

        Returns
        str: The path to the image file.
        """
        return self.image_path

    def set_image_path(self, path):
        """
        Sets the path to the image file and updates the image directory.

        Parameters
        path (str): The path to the image file.

        Returns
        None
        """
        self.image_path = path
        self.image_dir = os.path.dirname(self.image_path)

    def get_image_dir(self):
        """
        Gets the directory of the image file.

        Returns
        str: The directory of the image file.
        """
        return self.image_dir

    def get_edited_image_path(self):
        return self.edited_image_path

    def set_edited_image_path(self, path):
        self.edited_image_path = path

    def get_edited_image_dir(self):
        return self.edited_image_dir

    def set_edited_image_dir(self, dir):
        self.edited_image_dir = dir

    def get_edited_image_name(self):
        return self.edited_image_name

    def set_edited_image_name(self, name):
        self.edited_image_name = name

    def load_image(self, image_path):
        """
        Loads an image from the given path.

        Parameters
        image_path (str): The path to the image file.

        Returns
        ImageTk.PhotoImage: The loaded image object.
        """
        # Load image logic
        # Set edited image path to loaded image path by default
        self.set_edited_image_dir(os.path.dirname(image_path))
        self.image = cv2.imread(image_path)
        self.edited_image = self.image.copy()

    def get_image(self):
        """
        Gets the loaded image object.

        Returns
        OpenCV image: The loaded image object.
        """
        return self.image

    def get_edited_image(self):
        """
        Gets the edited image object.

        Returns
        ImageTk.PhotoImage: The edited image object or None if no image is loaded.
        """
        return self.edited_image

    def get_edited_image_as_tk(self):
        """
        Gets the edited image object as a tkinter photoimage object.

        Applies any scaling or rotation before converting to tkinter photoimage.

        Returns
        ImageTk.PhotoImage: The edited scaled image object in PhotoImage format.
        """
        if self.image is None:
            return None  # No image loaded yet
        tk_img = self.get_edited_scaled_image_as_tk()
        return tk_img

    def get_tk_photoimage(self):
        """
        Gets the loaded image converted to a tkinter photoimage object.

        This method converts the loaded image object to a tkinter photoimage
        object, which is an image format used by tkinter for displaying
        images.

        Returns
        ImageTk.PhotoImage: The loaded image object in PhotoImage format.
        """
        if self.image is None:
            return None  # No image loaded yet
        return self.opencv_to_tk(self.image)

    def get_edited_scaled_image_as_pil(self):
        """
        Gets the edited scaled image object as a PIL image object.

        Returns:
            PIL.Image: The converted PIL image object.
        """
        if self.scale_factor == 1.0:  # No need for scale operation if scale_factor == 1
            return self.opencv_to_pil(self.edited_image)

        # Convert edited_image in opencv format to pil image
        pil_img = self.opencv_to_pil(self.edited_image)

        # Calculate scaled dimensions from stored scale_factor
        scaled_width = int(pil_img.width * self.scale_factor)
        scaled_height = int(pil_img.height * self.scale_factor)

        # Create a copy of the scaled image
        resz_img = pil_img.resize((scaled_width, scaled_height))

        # Convert to PhotoImage type
        tk_img = ImageTk.PhotoImage(resz_img)
        # Clean up unused images
        pil_img = None
        return resz_img

    def get_edited_scaled_image_as_tk(self):
        """
        Gets the edited scaled image object as a tkinter photoimage object.

        Returns:
            ImageTk.PhotoImage: The edited scaled image object in PhotoImage format.
        """
        if self.scale_factor == 1.0:  # No need for scale operation if scale_factor == 1
            return self.opencv_to_tk(self.edited_image)

        # Convert edited_image in opencv format to pil image
        pil_img = self.opencv_to_pil(self.edited_image)

        # Calculate scaled dimensions from stored scale_factor
        scaled_width = int(pil_img.width * self.scale_factor)
        scaled_height = int(pil_img.height * self.scale_factor)

        # Create a copy of the scaled image
        resz_img = pil_img.resize((scaled_width, scaled_height))

        # Convert to PhotoImage type
        tk_img = ImageTk.PhotoImage(resz_img)
        # Clean up unused images
        pil_img = None
        resz_img = None
        return tk_img

    def opencv_to_pil(self, image):
        """
        Converts an OpenCV image to a PIL image.

        Parameters
        image (ndarray): The OpenCV image to be converted.

        Returns
        PIL.Image: The converted PIL image.
        None if the input image is not a valid OpenCV image.
        """
        if not self.is_opencv_image(image):
            print("Input image is not a valid OpenCV image.")
            return None
        # OpenCV uses BGR format, PIL uses RGB
        color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # Convert to PIL Image - from BGR to RGB format
        pil_image = Image.fromarray(color_coverted)
        return pil_image

    def opencv_to_tk(self, image):
        """
        Converts an OpenCV image to a tkinter photoimage object.

        Parameters
        image (ndarray): The OpenCV image to be converted.

        Returns
        ImageTk.PhotoImage: The converted tkinter photoimage object.
        None if the input image is not a valid OpenCV image.
        """
        if not self.is_opencv_image(image):
            print("Input image is not a valid OpenCV image.")
            return None
        pil_image = self.opencv_to_pil(image)
        tk_image = ImageTk.PhotoImage(image=pil_image)
        pil_image = None  # Clean up unused image
        return tk_image

    def is_opencv_image(self, image):
        """
        Checks if the given image is an OpenCV image.

        OpenCV images are represented as numpy arrays. So we check if the image
        is a numpy array and has either 2 or 3 dimensions. A 2D array is used
        for greyscale images and a 3D array is used for color images.
        This is the basic check to perform to see if the image is in OpenCV 
        format. It does not check if the image is a valid OpenCV image.

        Parameters
        image (ndarray): The image to be checked.

        Returns
        bool: True if the image is an OpenCV image, False otherwise.
        """
        # Check if the image is an OpenCV image
        is_opencv_img = False
        if isinstance(image, np.ndarray):
            if image.ndim == 2:  # 2D array - used for greyscale images
                is_opencv_img = True
            elif image.ndim == 3:  # 3D array - used for color images
                is_opencv_img = True
        return is_opencv_img

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

    def set_scale_factor(self, scale_factor):
        """
        Sets the scale factor for scaling the image.

        Parameters:
            scale_factor (float): The scale factor to be set.

        Returns:
            None
        """
        self.scale_factor = scale_factor

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
    def crop_image(self, start_x, start_y, end_x, end_y):
        # Crop image logic
        self.edited_image = self.image[start_y: end_y, start_x: end_x].copy()

    def get_edited_image(self):
        """
        Gets the edited image object.

        Returns
        ImageTk.PhotoImage: The edited image object or None if no image is loaded.
        """
        return self.edited_image

    def set_rotation_angle(self, angle):
        # Set rotation angle
        self.rotation_angle = angle

    def get_rotation_angle(self):
        return self.rotation_angle

    def rotate_image(self, angle):
        """
        Rotates the image.

        Parameters
        angle (int): The angle to rotate the image by.

        Returns
        None
        """
        # Rotate image logic
        # angle is the amount to rotate the image by
        if angle == 0:
            return  # No rotation required
        # Set the stored rotation of the image
        self.rotation_angle = (self.rotation_angle + angle) % 360
        if self.rotation_angle < 0:
            self.rotation_angle += 360

        img = self.edited_image.copy()
        # Get current image dimensions
        height, width = img.shape[:2]
        image_centre = (width // 2, height // 2)
        # Get rotation matrix - Positive values mean counter-clockwise rotation.
        # Convert standard angle - 0 to +360 in clockwise direction to opposite
        # for cv2.getRotationMatrix2D() as it uses + angle for ccw rotation
        angle = -1 * angle
        rotation_matrix = cv2.getRotationMatrix2D(image_centre, angle, 1.0)

        # Get cos and sin values from the rotation matrix
        rotated_cos = abs(rotation_matrix[0, 0])
        rotated_sin = abs(rotation_matrix[0, 1])

        # Find the new width and height bounds of the rotated image
        bound_width = int((height * rotated_sin) + (width * rotated_cos))
        bound_height = int((height * rotated_cos) + (width * rotated_sin))

        # Re-centre the image within the new bounds
        rotation_matrix[0, 2] += bound_width / 2 - image_centre[0]
        rotation_matrix[1, 2] += bound_height / 2 - image_centre[1]

        # Rotate image
        self.edited_image = cv2.warpAffine(
            img, rotation_matrix, (bound_width, bound_height), flags=cv2.INTER_NEAREST)
        img = None  # Clean up unsued image

        # Get rotated image dimensions
        (rh, rw) = self.edited_image.shape[:2]

    def reset_image(self):
        # Reset all image edits
        self.edited_image = None
        self.edited_image = self.image.copy()
        self.crop_coords = None
        self.rotation_angle = 0
        self.scale_factor = 1.0

    def save_edited_image(self, image_path):
        """
        Handles saving the current edited image to the file system.

        Parameters
        image_path (str): The path to save the edited image to.

        Returns
        None
        """
        # Save edited image logic
        self.set_edited_image_dir(os.path.dirname(image_path))
        self.set_edited_image_name(os.path.basename(image_path))
        self.set_edited_image_path(image_path)
        image = self.get_edited_scaled_image_as_pil()
        image.save(image_path)
        print(f"ImageModel.save_edited_image(): Saved edited image to: {
            image_path}")
