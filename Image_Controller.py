# Image Controller Class
# The Controller handles the input from the user, processes it, and updates the
# Model and View.
# It acts as an intermediary between the Model and the View, receiving user
# input and updating the Model and View accordingly.
# The Controller is responsible for managing the data and the rules of the
# application. It notifies the View when the data changes, so the View can
# update itself accordingly.


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
        # Bind UI events to controller methods
        self.view.open_image_button.config(command=self.load_image)
        self.view.save_image_button.config(command=self.save_image)
        self.view.crop_image_button.config(command=self.crop_image)
        self.view.quit_button.config(command=self.quit_app)

    def load_image(self):
        # Handle loading image
        image_dir = self.model.get_image_dir()
        image_path = self.view.open_image_file(start_path=image_dir)
        self.model.set_image_path(image_path)
        self.model.load_image(image_path)
        image = self.model.get_image()
        self.view.display_image(image)

    def save_image(self):
        # Handle saving image
        print("Saving image")
        pass

    def crop_image(self):
        # Handle cropping image
        print("Cropping image")
        pass

    def resize_image(self):
        # Handle resizing image
        print("Resizing image")
        pass

    def quit_app(self):
        # Quit the application
        print("Quitting application")
        self.view.root.destroy()
