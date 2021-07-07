from django.urls import path
from .views import home, form_crearusuario, ver_usuarios, modRegistro, borrarconsulta

urlpatterns=[
    path('home', home, name='home'),
    path('form_crearusuario', form_crearusuario, name='form_crearusuario'),
    path('ver_usuarios', ver_usuarios,name='ver_usuarios'),
    path('modRegistro/<id>',modRegistro,name='modRegistro'),
    path('borrarconsulta/<id>', borrarconsulta, name='borrarconsulta'),
]