import uuid

from django.db import models


class Departament(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.name