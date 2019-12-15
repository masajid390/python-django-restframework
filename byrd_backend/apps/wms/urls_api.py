from django.conf.urls import url
from .views_api import (sku, sku_help, storage, storage_help, order, order_help)

urlpatterns = [
    url(r'sku/help', sku_help),
    url(r'sku/', sku),
    url(r'storage/help', storage_help),
    url(r'storage/', storage),
    url(r'order/help', order_help),
    url(r'order/', order)
]
