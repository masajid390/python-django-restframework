from rest_framework import status
from rest_framework.decorators import api_view
from byrd_backend.apps.wms.operations import OrderOperations
from byrd_backend.libs.api.utils import (ResponseData, ByrdResponse)


@api_view(['GET', 'POST'])
def order(request):
    try:
        data = ResponseData()
        operations = OrderOperations()

        if request.method == 'GET':
            data.result = operations.get_list(request.query_params.get('q', None))
            data.message = "Orders has been fetched successfully."
            return ByrdResponse.get_success_response(status.HTTP_200_OK, data)

        elif request.method == 'POST':
            data.result = operations.create(request.data)
            data.message = "Order has been created/updated successfully."
            return ByrdResponse.get_success_response(status.HTTP_201_CREATED, data)

    except Exception as ex:
        return ByrdResponse.get_exception_response(ex)


@api_view(['GET'])
def help(request):
    try:
        data = ResponseData()
        if request.method == 'GET':
            data.result = OrderOperations().get_model_info()
            data.message = "Order endpoint object info."
            return ByrdResponse.get_success_response(status.HTTP_200_OK, data)

    except Exception as ex:
        return ByrdResponse.get_exception_response(ex)
