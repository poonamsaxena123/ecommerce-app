from django.contrib import admin
from store.models import Product ,variation
# Register your models here.



class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','stock','category','created_date','modified_date','is_available']
    prepopulated_fields={'slug':('name',)}


class AdminVariation(admin.ModelAdmin):
    list_display=['product','variation_category','variation_value','is_active']

admin.site.register(Product,AdminProduct)
admin.site.register(variation,AdminVariation)