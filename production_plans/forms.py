from django import forms
from .models import ProductionPlan


class ProductionPlanForm(forms.ModelForm):
    """
    Форма для добавления и редактирования планов производства.
    """
    class Meta:
        model = ProductionPlan
        fields = ['product', 'quantity', 'planned_date', 'status']
