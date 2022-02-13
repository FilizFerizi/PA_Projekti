class InvalidParameterException(Exception):
    def __init__(self, msg="Invalid Parameter Provided"):
        Exception.__init__(self, msg)


class NotFoundException(Exception):
    def __init__(self, msg="Not Found"):
        Exception.__init__(self, msg)


class AlreadyExistsException(Exception):
    def __init__(self, msg="Already Exists"):
        Exception.__init__(self, msg)
