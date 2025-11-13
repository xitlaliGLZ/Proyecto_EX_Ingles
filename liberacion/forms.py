
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Estudiante

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, label="Contraseña")
    nombre = forms.CharField(max_length=100, label="Nombre completo")
    matricula = forms.CharField(max_length=20, label="Matrícula")
    nivel_ingles = forms.CharField(max_length=50, label="Nivel de inglés")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'nombre', 'matricula', 'nivel_ingles']
        labels = {
            'username': 'Usuario',
            'email': 'Correo institucional',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@pabellon.tecnm.mx'):
            raise ValidationError("Solo se permite correo institucional (@pabellon.tecnm.mx)")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo ya está registrado.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya existe.")
        return username

    def clean_matricula(self):
        matricula = self.cleaned_data.get('matricula')
        if Estudiante.objects.filter(matricula=matricula).exists():
            raise ValidationError("Esta matrícula ya está registrada.")
        return matricula

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            Estudiante.objects.create(
                usuario=user,
                nombre=self.cleaned_data['nombre'],
                matricula=self.cleaned_data['matricula'],
                nivel_ingles=self.cleaned_data['nivel_ingles']
            )
        return user

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'matricula', 'nivel_ingles']
        labels = {
            'nombre': 'Nombre completo',
            'matricula': 'Matrícula',
            'nivel_ingles': 'Nivel de inglés',
        }
