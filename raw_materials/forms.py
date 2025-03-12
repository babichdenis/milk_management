from django import forms
from .models import RawMaterial


class RawMaterialForm(forms.ModelForm):
    """
    Форма для добавления и редактирования сырья.
    """
    class Meta:
        model = RawMaterial
        fields = ['supplier', 'quantity', 'fat_content', 'acidity',
                  'received_date', 'expiration_date', 'document_number', 'document_file']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'fat_content': forms.NumberInput(attrs={'class': 'form-control'}),
            'acidity': forms.NumberInput(attrs={'class': 'form-control'}),
            'received_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'document_number': forms.TextInput(attrs={'class': 'form-control'}),
            'document_file': forms.FileInput(attrs={'class': 'form-control'}),
        }
