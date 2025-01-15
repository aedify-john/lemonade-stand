from django import forms
from .models import MenuItem, Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['item', 'quantity']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than zero.")
        return quantity

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'description']

