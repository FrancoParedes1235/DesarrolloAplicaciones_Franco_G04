from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # Redirigir a la página de confirmación
            return redirect('confirmacion')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'registro_usuario.html', {'form': form})

def confirmacion(request):
    # Lógica para mostrar la página de confirmación
    return render(request, 'confirmacion.html')
