from django.db import models
from model_utils.models import TimeStampedModel


class SKU(TimeStampedModel):
    product_name = models.CharField(max_length=255)

    class Meta:
        app_label = "wms"
        verbose_name_plural = "SKUs"

    def __str__(self):
        return self.product_name
