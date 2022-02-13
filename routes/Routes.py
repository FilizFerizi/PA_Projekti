from tabulate import tabulate

from common.exceptions import NotFoundException
from routes.Common_Routes import CommonRoutes
from routes.Image_Route import ImageRoutes
from routes.Video_Route import VideoRoutes



class Routes:

    def __init__(self):
        self._current_route = None
        self._common_routes = CommonRoutes(self)
        self._video_routes = VideoRoutes(self)
        self._image_routes = ImageRoutes(self)

    def get_routes(self) -> dict:

        return {**self._common_routes.get(), **self._video_routes.get(),**self._image_routes.get()}

    def get_current_route(self):
        return self._current_route

    def set_current_route(self, route):
        self._current_route = route

    def route_wrapper(self, func, repeat=False, wait_to_continue=False, action=0):
        def inner_func():
            try:
                if action == 0:
                    func()
                elif action != 0:
                    func(action)

                if wait_to_continue:
                    input("Shtypni cfaredo butoni qe te vazhdoni ")

                if repeat:
                    repeat_choice = input(f"Deshironi te rrini ne kete sektor #{self.get_current_route()} ? p/j \n")
                    if repeat_choice and repeat_choice == 'p':
                        return self.route_wrapper(func, repeat)()

                self.navigator()
            except Exception as error:
                print(f"Error: {str(error)}")
                start_again_choice = None
                while True:
                    start_again_choice = input("Deshironi te filloni perseri p/j? ")
                    if start_again_choice != 'p' and start_again_choice != 'j':
                        print("Ju lutem shkruani  p ose j")
                        continue
                    break

                if start_again_choice == 'p':
                    return self.route_wrapper(func, repeat,action)()
                if start_again_choice == 'j':
                    self.navigator()

        return inner_func

    def start_app(self):
        self.navigator()

    def navigator(self):
        routes = self.get_routes()
        route_list = []
        for r in routes:
            route_list.append(r)

        route_options: dict = {}
        route_index: int = 0
        for r in route_list:
            route_options[route_index] = r
            route_index += 1

        print("Shkruani kodin e sektorit ne te cilin deshironi te vazhdoni")
        headers = ["Kodi i Sektorit", "Sektori"]
        print(tabulate(route_options.items(),headers=headers,tablefmt="fancy_grid"), )

        while True:
            try:
                route_input = int(input("Kodi: "))
                route = route_list[route_input]
                print(f"Sektori #{route.upper()} ")
                if routes.get(route):
                    self.set_current_route(route)
                    routes[route]()
                else:
                    raise NotFoundException()
            except NotFoundException as not_found:
                print(not_found)
                return self.navigator()
