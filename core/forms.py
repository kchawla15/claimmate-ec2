from django import forms
from .models import WarrantyItem

class WarrantyItemForm(forms.ModelForm):
    class Meta:
        model = WarrantyItem
        fields = ['store_name', 'product_type', 'warranty_duration_days', 'purchase_date', 'receipt_file']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
        }
