from django import forms

class SucursalForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    numero=forms.IntegerField()


class ProveedorForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()
    producto= forms.CharField(max_length=50)


class ClientesForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()

