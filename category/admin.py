from django.contrib import admin
from category.models import Category
# Register your models here.


@admin.register(Category)
class Category(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=['category_name','slug','description','cat_image']
