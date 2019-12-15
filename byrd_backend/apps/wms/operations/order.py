from django.db import transaction
from byrd_backend.apps.wms.models import Order
from byrd_backend.apps.wms.serializers import (OrderSerializer, OrderGetSerializer)
from byrd_backend.libs.operations import OperationManager
from byrd_backend.libs.exceptions import ByrdException
from .order_line import OrderLineOperations


class OrderOperations(OperationManager):

    def __init__(self):
        super().__init__(model=Order, serializer=OrderSerializer, serializer_get=OrderGetSerializer)

    def create_or_update(self, data):
        try:
            with transaction.atomic():

                lines_data = data.pop('lines', [])
                if len(lines_data) == 0:
                    message = 'Order must have more than 1 order line.'
                    raise ByrdException(message, [message])

                lines, picks = OrderLineOperations().get_create_update_lines_and_picks(lines_data)
                order = super().create_or_update(data)
                for line in lines:
                    order.lines.add(line)

                return {
                    'order': self.detail(order.id),
                    'picks': picks
                }
        except Exception as ex:
            raise ex

    def create(self, data):
        if data.get('id', None):
            message = 'Update order is not allowed. Please create new order or use sale return.'
            raise ByrdException(message, [message])
        return self.create_or_update(data)

    def get_list(self, query=None):
        queryset = None
        if query:
            queryset = self.filter_by_kwargs(customer_name__contains=query)
        return super().get_list(queryset)
