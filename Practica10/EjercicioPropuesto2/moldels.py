from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    correo = models.EmailField(unique=True)
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    contrasena = models.CharField(max_length=100)
    intereses = models.ManyToManyField('Interes')

class Interes(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
