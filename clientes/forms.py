from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre', 'descripcion', 'logo', 'link', 'ck', 'inicio', 'fin', 'noc', 'soc', 'poc', 'boc']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de cliente'}), 
            'descripcion': forms.Textarea(attrs={'class':'form-control mt-3','rows':3, 'placeholder':'Descripción de cliente'}), 
            'logo': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}), 
            'link': forms.URLInput(attrs={'class':'form-control', 'placeholder':'Sitio web de cliente'}),
            'ck': forms.TextInput(attrs={'class':'form-control', 'size':10, 'maxlength':10 ,'placeholder':'Ck cliente'}),
            'inicio': forms.DateInput(format='%d/%m/%Y', attrs={'class':'form-control', 'placeholder':'dd/mm/aa'}),
            'fin': forms.DateInput(format='%d/%m/%Y', attrs={'class':'form-control', 'placeholder':'dd/mm/aa'}),
            'noc': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'NOC'}),
            'soc': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'SOC'}),
            'poc': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'POC'}),
            'boc': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'BOC'}),
        }

        labels = {
            'nombre':'', 
            'descripcion':'',
            'logo':'',
            'link':'',
            'ck':'',
            'inicio':'',
            'fin':'',
        }