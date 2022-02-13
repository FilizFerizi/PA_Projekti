from controllers.Video_Controller import VideoController
from routes.IRoute import IRoute


class VideoRoutes(IRoute):
    _routes: {}

    def __init__(self, _root):
        content_controller = VideoController()
        self._routes = {
            "Downloadoni video": _root.route_wrapper(content_controller.create_new,True,False, 1),
            "Ruaj thumbnailat e videove": _root.route_wrapper(content_controller.create_new,True,False, 2),
            "Downloadoni video dhe ruaj thumbnailat e videove": _root.route_wrapper(content_controller.create_new,True,False, 3),
        }

    def get(self):
        return self._routes
