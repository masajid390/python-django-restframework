from django.db import models
from model_utils.models import TimeStampedModel
from .order_line import OrderLine


class Order(TimeStampedModel):
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    lines = models.ManyToManyField(OrderLine, blank=True, null=True)

    class Meta:
        app_label = "wms"
        verbose_name_plural = "Orders"
