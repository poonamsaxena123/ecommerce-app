from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=10)
    slug=models.SlugField(max_length=10)
    description=models.TextField(max_length=10,blank=True)
    price=models.IntegerField()
    image=models.ImageField(upload_to='photos/products')
    stock=models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date= models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    def get_url(self):
        return reverse('product_detail',args=[self.category.slug,self.slug])

   
    
    def is_in_stock(self):
        return self.stock > 0


class variation(models.Model):
    variation_cat_choice=(
        ('color','color'),
        ('size','size')
    )
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    variation_category=models.CharField(max_length=100,choices=variation_cat_choice)
    variation_value=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    created_date=models.DateField(auto_now_add=True)


    def __unicode__(self):
        return self.product