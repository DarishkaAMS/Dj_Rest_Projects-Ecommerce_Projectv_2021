from django.urls import path
from . import views


app_name = 'store'

urlpatterns = [
    path('', views.product_list_view, name='all_products'),
    path('item/<slug:slug>/', views.product_detail_view, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list_view, name='category_list'),
]
