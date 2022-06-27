from operator import ifloordiv
from django.db import models

# Create your models here.





class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    CONSULTAS = (
    (0, "Consulta"),
    (1, "Reclamo"),
    (2, "Sugerencias"),
    (3, "Felicitaciones")
)

    tipo_consulta = models.IntegerField(choices=CONSULTAS)
    mensaje = models.TextField()
    
   
    

        
    
    def __str__(self):
        return self.tipo_consulta



class Tests(models.Model):
    idhrs_disposr = models.AutoField(primary_key=True)
    fechar = models.DateField()
    horar = models.TimeField()
    detaller = models.CharField(max_length=45)
    fec_creacionr = models.DateTimeField()
    precior = models.IntegerField(blank=True, null=True)
    horassr = models.TimeField()
    class Meta:
        managed = False
        db_table = 'tests'