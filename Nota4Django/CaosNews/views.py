from django.shortcuts import redirect, render
from .models import Registrarse
from .forms import Registroform
# Create your views here.

def home(request):
    return render(request, 'home.html')

def form_crearusuario(request):
    registro = Registrarse.objects.all()
    if request.method=='POST':
        registro_form = Registroform(request.POST,request.FILES)
        if registro_form.is_valid():
            registro_form.save()
            return redirect('home')
    else:
        registro_form = Registroform()
    return render(request, 'CaosNews/form_crearusuario.html', {'registro_form':registro_form, 'datos':registro})


def ver_usuarios(request):
    registro = Registrarse.objects.all()
    if request.method=='POST':
        registro_form = Registroform(request.POST)
        if registro_form.is_valid():
            registro_form.save()
            return redirect('home')
    else:
        registro_form = Registroform()
    return render(request, 'CaosNews/ver_usuarios.html', {'registro_form':registro_form, 'datos':registro})

def modRegistro(request,id):
    registro = Registrarse.objects.get(rut_colaborador=id)

    datos = {
        'form':Registroform(instance=registro)
    }
    if request.method == 'POST':
        formulario = Registroform(request.POST, request.FILES, instance = registro)
        if formulario.is_valid:
            formulario.save()
            return redirect('home')
    return render(request, 'CaosNews/modRegistro.html',datos)

    
def borrarconsulta(request,id):
    registro = Registrarse.objects.get(rut_colaborador=id)
    registro.delete()
    return redirect('home')