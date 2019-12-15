from django.db import models
from model_utils.models import TimeStampedModel
from django.core.validators import MinValueValidator
from .sku import SKU


class OrderLine(TimeStampedModel):
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        app_label = "wms"
        verbose_name_plural = "Order Lines"
