from django.db import models

# Create your models here.

op_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencias"],
    [3, "Felicitaciones"]

]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=op_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

