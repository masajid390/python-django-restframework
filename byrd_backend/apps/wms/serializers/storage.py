from rest_framework import serializers
from byrd_backend.apps.wms.models import Storage


class StorageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storage
        exclude = ('created', 'modified')


class StorageGetSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(source="stock", read_only=True)

    class Meta:
        model = Storage
        fields = ('id', 'sku', 'quantity')
