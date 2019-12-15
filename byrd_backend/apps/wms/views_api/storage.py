from rest_framework import status
from rest_framework.decorators import api_view
from byrd_backend.apps.wms.operations import StorageOperations
from byrd_backend.libs.api.utils import (ResponseData, ByrdResponse)


@api_view(['GET', 'POST', 'DELETE'])
def storage(request):
    try:
        data = ResponseData()
        operations = StorageOperations()

        if request.method == 'GET':
            data.result = operations.get_list()
            data.message = "Storage list has been fetched successfully."
            return ByrdResponse.get_success_response(status.HTTP_200_OK, data)

        elif request.method == 'POST':
            instance = operations.create_or_update(request.data)
            data.result = operations.detail_by_instance(instance)
            data.message = "Storage has been created/updated successfully."
            return ByrdResponse.get_success_response(status.HTTP_201_CREATED, data)

        elif request.method == 'DELETE':
            operations.delete(request.query_params.get('id', None))
            data.message = "Storage has been deleted successfully."
            return ByrdResponse.get_success_response(status.HTTP_200_OK, data)

    except Exception as ex:
        return ByrdResponse.get_exception_response(ex)


@api_view(['GET'])
def help(request):
    try:
        data = ResponseData()
        if request.method == 'GET':
            data.result = StorageOperations().get_model_info()
            data.message = "Storage endpoint object info."
            return ByrdResponse.get_success_response(status.HTTP_200_OK, data)

    except Exception as ex:
        return ByrdResponse.get_exception_response(ex)
