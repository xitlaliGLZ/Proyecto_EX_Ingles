from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.portada, name='portada'),  # Portada pública
    path('home/', views.home, name='home'),   # Vista protegida
    path('solicitar/', views.solicitar_liberacion, name='solicitar'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('panel/', views.panel_admin, name='panel'),
    path('eliminar/<int:estudiante_id>/', views.eliminar_solicitud, name='eliminar_solicitud'),  # ✅ nueva ruta
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('firmar/', views.firmar_contrato, name='firmar_contrato'),
    path('contrato_pdf/', views.contrato_pdf, name='contrato_pdf'),  # ✅ nueva ruta
    path('firmar/', views.firmar_contrato, name='firmar_contrato'),
    path('firmar_admin/<int:id>/', views.firmar_contrato_admin, name='firmar_contrato_admin'),
    path('panel/', views.panel_admin, name='panel_admin'),  # ✅ esta ruta faltaba
    path('redirigir/', views.redireccion_rol, name='redirigir'),  # ✅ Redirección por rol
]  







