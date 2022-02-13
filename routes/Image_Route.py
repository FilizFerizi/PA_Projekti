from controllers.Video_Controller import VideoController
from routes.IRoute import IRoute


class ImageRoutes(IRoute):
    _routes: {}

    def __init__(self, _root):
        content_controller = VideoController()
        self._routes = {
            "Downloadoni Foto": _root.route_wrapper(content_controller.create_new, True),
            "Zvogelo Foto": _root.route_wrapper(content_controller.create_new,  True),
        }

    def get(self):
        return self._routes
