from byrd_backend.apps.wms.models import SKU
from byrd_backend.apps.wms.serializers import SKUSerializer
from byrd_backend.libs.operations import OperationManager


class SKUOperations(OperationManager):

    def __init__(self):
        super().__init__(model=SKU, serializer=SKUSerializer)
