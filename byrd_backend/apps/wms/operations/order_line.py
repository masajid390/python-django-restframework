from django.db import transaction
from byrd_backend.apps.wms.models import OrderLine
from byrd_backend.apps.wms.serializers import OrderLineSerializer
from byrd_backend.libs.operations import OperationManager
from byrd_backend.libs.exceptions import ByrdException


class OrderLineOperations(OperationManager):

    def __init__(self):
        super().__init__(model=OrderLine, serializer=OrderLineSerializer)

    def get_list(self, order=None):
        if not order:
            message = 'Missing order.'
            raise ByrdException(message, [message])
        order = self.get_instance(order)
        return super().get_list(self.filter_by_kwargs(order=order.id))

    def get_create_update_lines_and_picks(self, lines_data):
        from byrd_backend.apps.wms.operations import StorageOperations
        """
        Would create lines and update stock under stock
        :param lines_data:
        :param prev_lines:
        :return: A Tuple with 1st item as lines and 2nd as picks
        """
        try:
            stock_operations = StorageOperations()
            if self.is_valid(lines_data, True, True):
                lines, picks = [], []
                for line_data in lines_data:
                    line = self.create_or_update(line_data)
                    lines.append(line.id)
                    picks = picks + stock_operations.get_picks(line)
                return lines, picks
        except Exception as ex:
            raise ex
