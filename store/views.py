from django.shortcuts import render

from .models import Category, Product


def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def category_dropdown_view(request):
    return {
        'categories': Category.objects.all()
    }
