from .byrd_exception import ByrdException


class InvalidSerializer(ByrdException):
    def __init__(self, message, errors=None):
        super().__init__(message, errors)
