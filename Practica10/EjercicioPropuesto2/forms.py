from django import forms
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    confirmar_contrasena = forms.CharField(widget=forms.PasswordInput)
    intereses = forms.ModelMultipleChoiceField(
        queryset=Interes.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Usuario
        fields = ['nombre', 'fecha_nacimiento', 'direccion', 'correo', 'sexo', 'contrasena', 'confirmar_contrasena', 'intereses']
