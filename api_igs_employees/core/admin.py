from django.contrib import admin

# Register your models here.
from api_igs_employees.core.models import Departament, Employee

admin.site.register(Departament)
admin.site.register(Employee)