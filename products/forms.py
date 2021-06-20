from django import forms

from products.models import ProductCategory


class ProductCategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите название категории'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите описание категории'}))

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')