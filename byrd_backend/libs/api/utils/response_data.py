from .byrd_object import ByrdObject


class ResponseData(ByrdObject):
    def __init__(self):
        self.message = ""
        self.result = None
        self.successful = False
        self.errors = None
