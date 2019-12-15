from rest_framework.response import Response
from rest_framework import status
from .response_data import ResponseData
from byrd_backend.libs.exceptions import (InvalidSerializer, ByrdException)


class ByrdResponse:
    """ Uses to send api response back to the client """

    @staticmethod
    def get_success_response(_status, data=None):
        """
        :param _status: rest_framework.status
        :param data: Type of ResponseData
        :return:
        """
        _message = 'Action was successful.'
        if not data:
            data = ResponseData()
            data.message = _message
        if not data.message:
            data.message = _message
        data.successful = True
        return Response(status=_status, data=data.to_dict())

    @staticmethod
    def get_invalid_serializer_response(errors, message=""):
        data = ResponseData()
        data.errors = errors
        data.message = message
        return Response(status=status.HTTP_200_OK, data=data.to_dict())

    @staticmethod
    def get_exception_response(ex):
        if type(ex) == InvalidSerializer:
            return ByrdResponse.get_invalid_serializer_response(ex.errors, ex.message)
        if type(ex) != ByrdException:
            ex = ByrdException(str(ex), getattr(ex, 'errors', None))
        data = ResponseData()
        data.message = ex.message
        data.errors = ex.errors
        return Response(status=status.HTTP_400_BAD_REQUEST, data=data.to_dict())
