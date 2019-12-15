from django.db import transaction
from django.db.models import Sum
from byrd_backend.apps.wms.models import Storage
from byrd_backend.apps.wms.serializers import (StorageSerializer, StorageGetSerializer)
from byrd_backend.libs.operations import OperationManager
from byrd_backend.libs.exceptions import ByrdException


class StorageOperations(OperationManager):

    def __init__(self):
        super().__init__(model=Storage, serializer=StorageSerializer, serializer_get=StorageGetSerializer)

    def create_or_update(self, data):
        data['stock'] = data.pop('quantity', 0)
        return super().create_or_update(data)

    def validate_stock(self, sku, quantity):
        if self.filter_by_kwargs(sku=sku).aggregate(Sum('stock')).get('stock__sum', 0) < quantity:
            message = 'Out of stock or limited stock.'
            raise ByrdException(message, [message])

    def update_stock(self, storage, quantity):
        storage.stock = storage.stock + quantity
        storage.save()

    def get_picks(self, line):
        try:
            with transaction.atomic():
                self.validate_stock(line.sku, line.quantity)
                picks = []
                storage_queryset = self.filter_by_kwargs(sku=line.sku).order_by('stock')
                remaining_pick = line.quantity

                for storage in storage_queryset:
                    if remaining_pick > 0:
                        quantity = remaining_pick
                        remaining_pick = remaining_pick - storage.stock
                        if remaining_pick > 0:
                            quantity = storage.stock

                        if quantity > 0:
                            picks.append({
                                'id': storage.id,
                                'quantity': quantity
                            })
                        self.update_stock(storage, quantity * -1)
                        if remaining_pick <= 0:
                            break
                return picks
        except Exception as ex:
            raise ex
