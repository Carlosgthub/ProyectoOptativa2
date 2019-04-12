from django.db import models

# Create your models here.
class Carrera(models.Model):
    nombre=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Alumno(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    carrera=models.ForeignKey(Carrera, on_delete=models.CASCADE)
    def __str__(self):
        return 'No. de control:' + str(self.id)+ ' ' +' ------->>>>> ' + self.nombre + ' ' + self.apellido

class Docente(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre+ ' ' + self.apellido

class Materia(models.Model):
    nombre=models.CharField(max_length=100)
    creditos=models.IntegerField()
    maestro=models.ForeignKey(Docente, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    materia=models.ForeignKey(Materia, on_delete=models.CASCADE)
    alumno=models.ForeignKey(Alumno, on_delete=models.CASCADE)
    def __str__(self):
        return self.materia.nombre