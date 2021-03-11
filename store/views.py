from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product':product})


def category_dropdown_view(request):
    return {
        'categories': Category.objects.all()
    }
