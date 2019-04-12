from django.contrib import admin
from .models import Carrera, Alumno, Docente, Materia, Grupo
# Register your models here.
admin.site.register(Carrera)
admin.site.register(Alumno)
admin.site.register(Docente)
admin.site.register(Materia)
admin.site.register(Grupo)