from rest_framework import serializers
from byrd_backend.apps.wms.models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = ('created', 'modified')


class OrderGetSerializer(serializers.ModelSerializer):
    lines = serializers.SerializerMethodField()

    def get_lines(self, order):
        from byrd_backend.apps.wms.serializers import OrderLineSerializer
        return OrderLineSerializer(order.lines, many=True).data

    class Meta:
        model = Order
        fields = ('id', 'customer_name', 'lines')
