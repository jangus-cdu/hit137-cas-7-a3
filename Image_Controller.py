# Controller
# The Controller handles the input from the user, processes it, and updates the
# Model and View.
# It acts as an intermediary between the Model and the View,
# receiving user input and updating the Model and View accordingly.
# The Controller is responsible for managing the data and the rules of the
# application. It notifies the View when the data changes, so the View can
# update itself accordingly.
# The Controller is responsible for handling user input, processing it, and
# updating the Model and View accordingly. It acts as an intermediary between
# the Model and the View, receiving user input and updating the Model and View


class ImageController:

    def __init__(self, model, view):
        self.model = model  # Instance of ImageModel.
        self.view = view  # Instance of ImageView.
        self.bind_events()
        self.view.button.config(command=self.update_name)

    def load_image(self):
        # Handle loading image
        pass

    def save_image(self):
        # Handle saving image
        pass

    def apply_filter(self, filter_type):
        # Handle applying filter
        pass

    def resize_image(self):
        # Handle resizing image
        pass

    def rotate_image(self):
        # Handle rotating image
        pass

    def bind_events(self):
        # Bind UI events to controller methods
        pass

    def update_name(self):
        name = self.view.get_input()
        self.model.set_name(name)
        self.view.set_display(f"Hello, {self.model.get_name()}!")
