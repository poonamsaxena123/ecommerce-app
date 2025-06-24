from django.shortcuts import render,get_object_or_404
from store.models import Product
from category.models import Category
# Create your views here.
from carts.models import CartItem,Cart
from carts.views import _cart_id
from django.http import HttpResponse
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.db.models import Q

def store(request,category_slug=None):
    category=None
    product=None
    if category_slug!=None:
        category= get_object_or_404(Category,slug=category_slug)
        product = Product.objects.filter(category=category,is_available=True)
        paginator= Paginator(product,1)
        page=request.GET.get('page')
        paged_product=paginator.get_page(page)
        product_count=product.count()
    else:
        product =Product.objects.all().filter(is_available=True).order_by('id')
        
        paginator = Paginator(product,1)
        page= request.GET.get('page')
        paged_product =paginator.get_page(page)
        product_count=product.count()
    context={
                "product":paged_product,
                'product_count':product_count
            }

    return render(request, "store/store.html",context)
    

def product_detail(request,category_slug,product_slug):
    try:
    
        single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
        in_cart= CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()
       

    except Exception as e:
        raise e
    context={
        'single_product':single_product,
        'in_cart':in_cart
    }

    return render(request,"store/product_detail.html",context)


def search(request):
    product_count=0
    product=None
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword :
            product =Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(name__icontains=keyword))
            product_count=product.count()
        context={
            'product' :product,
            'product_count':product_count
        }
    return render(request,"store/store.html",context)