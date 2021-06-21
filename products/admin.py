from django.contrib import admin
from products.models import ProductCategory, Product


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = (('name', 'category'), 'image', 'description', ('price', 'quantity'))
    readonly_fields = ('description',)
    ordering = ('price',)
    search_fields = ('name',)