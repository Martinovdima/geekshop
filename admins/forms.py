from django import forms

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from products.forms import ProductCategoryForm, ProductForm
from products.models import ProductCategory, Product


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image','first_name', 'last_name', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': False}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': False}))


class ProductCategoryAdminForm(ProductCategoryForm):
    class Meta:
        model = ProductCategory
        fields = ('name', 'description')

class ProductAdminForm(ProductForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'quantity', 'category')