from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ['cliente', 'nombres', 'apellidos', 'cargo', 'nivel', 'email', 'telefono', 'celular', 'horario']
        widgets = {
            'cliente': forms.Select(attrs={'class':'form-control', 'placeholder':'Nombre de cliente'}), 
            'nombres': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripción de cliente'}), 
            'apellidos': forms.TextInput(attrs={'class':'form-control'}), 
            'cargo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sitio web de cliente'}),
            'nivel': forms.NumberInput(attrs={'class':'form-control', 'size':10, 'maxlength':10 ,'placeholder':'Ck cliente'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'dd/mm/aa'}),
            'telefono': forms.TextInput(attrs={'class':'form-control', 'placeholder':'dd/mm/aa'}),
            'celular': forms.TextInput(attrs={'class':'form-control', 'placeholder':'NOC'}),
            'horario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'POC'}),
        }