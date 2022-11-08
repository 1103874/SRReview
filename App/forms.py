from django import forms
from .models import SRList


class SRCreateForm(forms.ModelForm):
    class Meta:
        model = SRList
        fields = ['sr_type', 'region', 'dt', 'title', 'description', 'file_upload']

        widgets = {
            'sr_type': forms.RadioSelect(attrs={'class': ''}),
            'region' : forms.TextInput(attrs={'class':'form-control'}),
            'dt' : forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'rows': 10}),
        }