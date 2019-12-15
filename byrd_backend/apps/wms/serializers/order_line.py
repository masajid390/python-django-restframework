from rest_framework import serializers
from byrd_backend.apps.wms.models import OrderLine


class OrderLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderLine
        exclude = ('created', 'modified')
