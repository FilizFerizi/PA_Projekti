from routes.IRoute import IRoute


class CommonRoutes(IRoute):
    _routes: dict = {}

    def __init__(self, _root):
        self._routes = {
            "Exit": self.exit_app
        }

    def exit_app(self):
        print("App Exited")
        exit()

    def get(self) -> dict:
        return self._routes
