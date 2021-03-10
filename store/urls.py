from django.urls import path
from . import views


app_name = 'store'

urlpatterns = [
    path('', views.product_list_view, name='all_products'),
]
