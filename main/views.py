from django.http import HttpResponse
from django.shortcuts import render
from main.models import Category, Product

# Create your views here.
def all_product(request):
    products = Product.objects.all()
    #select * from product;
    print(locals())
    return render(request, 'product.html', locals())

def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categoryes': categories})