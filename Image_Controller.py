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

        # self.view.image_canvas_original.bind(
        #     "<ButtonPress-1>", self.on_mouse_press)
        # self.view.image_canvas_original.bind("<B1-Motion>", self.on_mouse_drag)
        # self.view.image_canvas_original.bind(
        #     "<ButtonRelease-1>", self.on_mouse_release)

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

    def quit_app(self):
        # Quit the application
        print("Quitting application")
        self.view.root.destroy()

    # def on_mouse_press(self, event):
    #     self.view.start_x = event.x
    #     self.view.start_y = event.y
    #     if self.view.rect:
    #         self.view.image_canvas_original.delete(self.view.rect)
    #     self.view.rect = self.view.image_canvas_original.create_rectangle(
    #         self.view.start_x, self.view.start_y, self.view.start_x, self.view.start_y, outline="red")

    # def on_mouse_drag(self, event):
    #     if self.view.rect:
    #         self.view.image_canvas_original.coords(
    #             self.view.rect, self.view.start_x, self.view.start_y, event.x, event.y)

    # def on_mouse_release(self, event):
    #     if self.view.rect:
    #         self.handle_crop(
    #             self.view.start_x, self.view.start_y, event.x, event.y)

    # def handle_crop(self, start_x, start_y, end_x, end_y):
        # self.model.set_crop_coords(start_x, start_y, end_x, end_y)

    def crop_image(self):
        # Handle cropping image
        self.model.set_crop_coords(
            self.view.start_x, self.view.start_y, self.view.end_x, self.view.end_y)
        cropped_image = self.model.get_cropped_image()
        if cropped_image:
            self.view.update_edited_image(cropped_image)

    # def crop_image(self):
        # Handle cropping image
        # print("Cropping image")
        # pass

    def resize_image(self):
        # Handle resizing image
        print("Resizing image")
        pass
