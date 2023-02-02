from django.contrib import admin

from .models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)
# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    # readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name', 'price')


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
