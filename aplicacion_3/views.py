from django.shortcuts import render
from aplicacion_3.models import registroUsuarios
from .forms import registroForm

def primeraFuncion(request):
    return render(request, 'landing.html')


# Tarea 4 individual
def formularioContacto(request):
    data = {
        'form': registroForm()
    }
    if request.method == 'POST':
        formulario = registroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "USUARIO REGISTRADO !!!"
        else:
            data["form"] = formulario

    return render(request, 'registro.html', data)
# Tarea 4 individual


def informeUsuarios(request):
     #'usuarios' es una instancia de la clase "registroUsuarios" definida en models.py
    usuarios = registroUsuarios.objects.all()
    #data = {
    #    'usuarios': usuarios
    #}
    return render(request, 'salida.html', {'usuarios': usuarios})