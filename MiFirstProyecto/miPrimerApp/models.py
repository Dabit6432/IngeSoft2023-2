from django.db import models

# Create your models here.
class  Grupo(models.Model):
  id_grupo  =  models.AutoField(primary_key=True)

class  Estudiante(models.Model):
  numCta  =  models.IntegerField(default=0, max_length=9)
  nombres  =  models.CharField(max_length=200)
  apellidos  =  models.CharField(max_length=200)
  edad = models.IntegerField(default=0, max_length=3)
  imagen = models.CharField(default=' ', max_length=1000)
  # Cada estudiante guarda el grupo en el que está inscrito
  grupo  =  models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return f'Nombre: {self.nombres}, Apellidos: {self.apellidos}, Edad: {self.edad}, Grupo: {self.grupo}, NumCta: {self.numCta}'