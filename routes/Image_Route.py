from controllers.Image_Controller import ImageController
from routes.IRoute import IRoute


class ImageRoutes(IRoute):
    _routes: {}

    def __init__(self, _root):
        content_controller = ImageController()
        self._routes = {
            "Downloadoni dhe zvogelo Foto": _root.route_wrapper(content_controller.create_new, True),
        }

    def get(self):
        return self._routes
