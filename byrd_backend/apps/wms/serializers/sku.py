from rest_framework import serializers
from byrd_backend.apps.wms.models import SKU


class SKUSerializer(serializers.ModelSerializer):

    class Meta:
        model = SKU
        exclude = ('created', 'modified')
