from django.shortcuts import render
from .forms import ContactoForms

# Create your views here.
def index(request):
    return render(request, 'index.html')


def contacto(request):
    data = {
        'form': ContactoForms()
    }

    if request.method == 'POST':
        formulario = ContactoForms(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["email"] = "Consulta guardada"
        
        else:
            data['form'] = formulario
    return render(request, 'index.html', data)