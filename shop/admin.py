import django
from django.contrib import admin
from shop.models import Catagory, Product

# Register your models here.
@admin(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display=['name', 'slug']
    prepopulated_filds={'slug':('name')}


@admin(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name', 'catagory', 'price', 'is_stock', 'publish_date']
    list_filter=['is_stock', 'is_active']
    list_editable=['price', 'is_active', 'is_stock']
