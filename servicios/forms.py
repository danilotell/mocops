from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = ['cliente', 'nocdis', 'noccap', 'nocmet', 'nocsim', 'nocinv', 'nocdescripcion', 
        'socsiem', 'socthreat', 'socrisk', 'soccomp', 'socinc', 'socfim', 'socdescripcion', 
        'poceh', 'pocgv', 'pocav', 'pocadm', 'pocapt', 'pochpot', 'poceducate', 'pochsas', 'pocdescripcion',
        'bocga', 'bocge', 'bocgi', 'bocri',  'boccump', 'bocplan', 'bocind', 'boccs', 'bocdescripcion']
        widgets = {
            'cliente': forms.Select(attrs={'class':'form-control', 'placeholder':'Nombre de cliente'}),
            'nocdis': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'NOC'}),
            'noccap': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'NOC'}),
            'nocmet': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'NOC'}),
            'nocsim': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'NOC'}),
            'nocinv': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'NOC'}),
            'nocdescripcion': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'NOC'}),

            'socsiem': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'SOC'}),
            'socthreat': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'SOC'}),
            'socrisk': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'SOC'}),
            'soccomp': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'SOC'}),
            'socinc': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'SOC'}),
            'socfim': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'SOC'}),
            'socdescripcion': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'SOC'}),

            'poceh': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'POC'}),
            'pocgv': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'POC'}),
            'pocav': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'POC'}),
            'pocadm': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'POC'}),
            'pocapt': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'POC'}),
            'pochpot': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'POC'}),
            'poceducate': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'POC'}),
            'pochsas': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'POC'}),
            'pocdescripcion': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'POC'}),

            'bocga': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'BOC'}),
            'bocge': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'BOC'}),
            'bocgi': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'BOC'}),
            'bocri': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'BOC'}),
            'boccump': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'BOC'}),
            'bocplan': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'BOC'}),
            'bocind': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'BOC'}),
            'boccs': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'BOC'}),
            'bocdescripcion': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'BOC'}),
        }