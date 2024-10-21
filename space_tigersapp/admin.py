from django.contrib import admin
from .models import Product, Customer

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'stock')

admin.site.register(Product)
admin.site.register(Customer)