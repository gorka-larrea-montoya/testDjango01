from django.contrib import admin
from .models import Departamento, Habilidad, Empleado
# Register your models here.
admin.site.register(Departamento)
admin.site.register(Habilidad)
admin.site.register(Empleado)