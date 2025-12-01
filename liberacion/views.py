from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Estudiante
from .forms import RegistroForm, EstudianteForm
from django.utils import timezone
from django.http import HttpResponse
from django.template.loader import get_template
import io
from xhtml2pdf import pisa
import os
from django.conf import settings

def firmar_contrato_admin(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        estudiante.firmado = True
        estudiante.fecha_firma = timezone.now()
        estudiante.save()
        # ✅ Después de firmar, redirige al panel admin
        return redirect('panel_admin')
    
def contrato_pdf(request):
    estudiante = request.user.estudiante
    template_path = 'liberacion/contrato_pdf.html'
    context = {
        'nombre': estudiante.nombre,
        'matricula': estudiante.matricula,
        'nivel': estudiante.nivel_ingles,
        'fecha_actual': estudiante.fecha_firma or ''
    }

    template = get_template(template_path)
    html = template.render(context)

    # ✅ Crear carpeta de destino si no existe
    output_dir = os.path.join(settings.MEDIA_ROOT, 'contratos')
    os.makedirs(output_dir, exist_ok=True)

    # ✅ Nombre del archivo con la matrícula
    filename = f"{estudiante.matricula}.pdf"
    file_path = os.path.join(output_dir, filename)

    # ✅ Guardar el PDF en archivo
    with open(file_path, "wb") as f:
        pisa_status = pisa.CreatePDF(io.BytesIO(html.encode("UTF-8")), dest=f)

    # ✅ También devolverlo al navegador
    with open(file_path, "rb") as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response


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

def firmar_contrato(request):
    estudiante = get_object_or_404(Estudiante, usuario=request.user)
    if request.method == 'POST':
        estudiante.firmado = True
        estudiante.fecha_firma = timezone.now()
        estudiante.save()
        mensaje = "Tu firma ha sido registrada correctamente."
        return render(request, 'liberacion/firmar_contrato.html', {
            'mensaje': mensaje,
            'fecha_actual': estudiante.fecha_firma
        })
    return render(request, 'liberacion/firmar_contrato.html', {
        'fecha_actual': timezone.now()
    })
