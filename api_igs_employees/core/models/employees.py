import uuid

from django.db import models

from api_igs_employees.core.models import Departament


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(max_length=150, blank=False, null=False)
    departament = models.ForeignKey(Departament, on_delete=models.SET_NULL, null=True, default=None, blank=True)

    def __str__(self):
        return self.name


