import django
from django.contrib import admin
from shop.models import Catagory, Product

# Register your models here.
# admin.site.register(Product)
# admin.site.register(Catagory)
@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display=['name']
    prepopulated_filds={'slug':('name')}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name', 'catagory', 'price', 'is_stock', 'published_date']
    list_filter=['is_active', 'is_stock' ]
    list_editable=['price', 'is_stock', 'is_stock']
