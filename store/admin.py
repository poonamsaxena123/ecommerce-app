from django.contrib import admin
from store.models import Product
# Register your models here.



class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','stock','category','created_date','modified_date','is_available']
    prepopulated_fields={'slug':('name',)}

admin.site.register(Product,AdminProduct)