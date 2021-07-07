from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Registrarse

class Registroform(forms.ModelForm):
    class Meta:
        model= Registrarse
        fields = ['rut_colaborador','imagen','nombre_completo' , 'telefono' , 'dirección', 'email' , 'pais' , 'contraseña']
        labels = {'rut_colaborador': 'Ingrese su RUT',
                'nombre_completo': 'Ingrese su Nombre Completo',
                'imagen':'Ingrese alguna imagen caracteristica',
                'telefono' : 'Ingrese su numero de telefono',
                'dirección': 'Ingrese su dirección',
                'email' : 'Ingrese su correo electronico',
                'pais' : 'Ingrese su pais',
                'contraseña' : 'Ingrese su Contraseña',}
        
        widgets={ 
            'rut_colaborador': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su rut sin Puntos y con Guion', 
                    'id': 'rut colaborador',
                    'name': 'rut colaborador',
                }
            ),
            'imagen':forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'name': 'imagen',
                    'id': 'imagen',
                    'accept':"imagen/*"
                }
            ), 
            'nombre_completo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su nombre completo', 
                    'id': 'nombre completo',
                    'name': 'nombre completo',
                    'onchange': 'MayusculaNombre()',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su numero de Telefono', 
                    'id': 'telefono',
                    'name': 'telefono',
                    'type': 'telefono',
                }
            ), 
            'dirección': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su direccion', 
                    'id': 'direccion',
                    'name': 'direccion',
                }
            ), 
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su Correo Electrónico', 
                    'id': 'email',
                    'name': 'email',
                    'type': 'email',
                    
                }
            ),
            'pais': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su País',
                    'id': 'pais',
                    'name': 'pais',
                }
            ),
            'contraseña': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su contraseña', 
                    'id': 'constraseña',
                    'name': 'contraseña',
                    'type':'password',
                }
            ), 
        }