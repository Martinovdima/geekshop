from django import forms

from products.models import ProductCategory, Product


class ProductCategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите название категории'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите описание категории'}))

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите название продукта'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите описание продукта'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите стоимость продукта'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите количество продукта'}))
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all())

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'quantity', 'category')