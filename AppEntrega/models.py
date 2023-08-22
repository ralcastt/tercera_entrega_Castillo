from django.db import models


class Sucursal(models.Model):
    nombre=models.CharField(max_length=50)
    numero=models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.numero}"

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Proveedor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    producto= models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

