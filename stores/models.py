import uuid
from django.db import models


class Store(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    store_name = models.CharField(max_length=19)
    store_owner = models.CharField(max_length=14)
