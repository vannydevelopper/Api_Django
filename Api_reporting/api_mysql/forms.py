from django import forms
from . models import Eleve

class eleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = '__all__'
        widgets = {
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
        }
