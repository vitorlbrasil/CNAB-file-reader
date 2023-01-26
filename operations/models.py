import uuid
from django.db import models


class Operation(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    type = models.PositiveSmallIntegerField()
    date = models.DateField()
    value = models.FloatField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()

    store = models.ForeignKey(
        "stores.Store",
        on_delete=models.CASCADE,
        related_name="operations",
    )
