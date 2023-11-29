from django import forms
from .models import Arrendatario


class ArrendatarioForm(forms.ModelForm):
    class Meta:
        model = Arrendatario
        fields = (
            "nombre",
            "apellido",
            "ci",
            "telefono",
            "direccion",
            "lugar_arrendar",
        )
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3 }),
            'lugar_arrendar': forms.Textarea(attrs={'rows': 3 })
        }
