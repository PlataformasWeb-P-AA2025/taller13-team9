from django.db import models


class Edificio(models.Model):
    CHOICES_TIPO = (
        ("reseidencial", "Resedencial"),
        ("comercial", "Comercial"),
    )

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=CHOICES_TIPO)

class Departamento(models.Model):
    nombre_propietario = models.CharField(max_length=100)
    costo = models.DecimalField(decimal_places=2, max_digits=10)
    num_cuartos = models.IntegerField()
    edificio = models.ForeignKey("Edificio", on_delete=models.CASCADE)
