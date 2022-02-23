from controllers.Image_Controller import ImageController
from routes.IRoute import IRoute


class ImageRoutes(IRoute):
    _routes: {}

    def __init__(self, _root):
        content_controller = ImageController()
        self._routes = {
            "Shkarko Foto": _root.route_wrapper(content_controller.create_new, True,True, 1),
            "Shkarko foton e zvogeluar": _root.route_wrapper(content_controller.create_new, True,False, 2),
            "Shkarko dhe zvogelo Foton ": _root.route_wrapper(content_controller.create_new, True,False, 3),
        }

    def get(self):
        return self._routes
