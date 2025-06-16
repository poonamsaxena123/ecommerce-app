from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def home(requset):
    print("request-",requset)
    print("request-",requset.body)
    product =Product.objects.all().filter(is_available=True)
    context={
        "product":product,
    }

    return render(requset, "home.html",context)
