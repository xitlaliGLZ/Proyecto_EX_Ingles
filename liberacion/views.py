from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Estudiante
from .forms import RegistroForm, EstudianteForm

def portada(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'liberacion/portada.html')

@login_required
def redireccion_rol(request):
    if request.user.is_staff:
        return redirect('panel')  # Panel para administradores
    elif hasattr(request.user, 'estudiante'):
        return redirect('home')   # Página para estudiantes
    else:
        return redirect('portada')  # Por si no tiene rol definido

@login_required
def home(request):
    return render(request, 'liberacion/home.html')

@login_required
def solicitar_liberacion(request):
    estudiante = request.user.estudiante
    if request.method == 'POST':
        # ✅ Agregamos request.FILES para manejar archivos
        form = EstudianteForm(request.POST, request.FILES, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('confirmacion')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'liberacion/solicitud.html', {'form': form})

def confirmacion(request):
    return render(request, 'liberacion/confirmacion.html')

@user_passes_test(lambda u: u.is_staff)
def panel_admin(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'liberacion/panel_admin.html', {'estudiantes': estudiantes})

@user_passes_test(lambda u: u.is_staff)
def eliminar_solicitud(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    estudiante.delete()
    return redirect('panel')

def registro(request):
    if request.method == 'POST':
        # ✅ Agregamos request.FILES aquí también
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'liberacion/registro.html', {'form': form})
