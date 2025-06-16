from category.models import Category

def manu_list(request):
    links=Category.objects.all()
    print("--", dict(link=links))
    return dict(link=links)