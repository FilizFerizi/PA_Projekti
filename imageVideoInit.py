from abc import ABC


class IMedia(ABC):

    @ABC.abstractmethod
    def media_method(self):
        pass


class Photo(IMedia):
    def __init__(self, name, link):
        self.name = name
        self.link = link

    def media_method(self):
        print("Une jam nje foto!")


class Video(IMedia):
    def __init__(self, name, link):
        self.name = name
        self.link = link

    def media_method(self):
        print("Une jam nje video!")


