from django import forms
from .models import registroUsuarios

class registroForm(forms.ModelForm):
    class Meta:
        model = registroUsuarios
        #fields = ['rut', 'nombre', 'apellido'] /// esto si quiero algunos campos. Alternativa, "all" 
        fields = '__all__'