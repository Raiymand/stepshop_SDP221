from django.urls import path

from mainapp.views import product, products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('product/', product, name='product'),
]
