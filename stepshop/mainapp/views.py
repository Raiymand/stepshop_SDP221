from django.shortcuts import render

from mainapp.models import Product


def get_data(**kawargs):
    links_menu = [
        {'link': 'index', 'name': 'Главное'},
        {'link': 'products:index', 'name': 'Продукты'},
        {'link': 'about', 'name': 'О нас'},
        {'link': 'contacts', 'name': 'Контакты'}
    ]
    context = {'links_menu': links_menu}
    context.update(**kawargs)
    return context


def index(request):
    title = "главное"
    prods = Product.objects.all()
    context = get_data(title=title, prods=prods)
    return render(request, 'index.html', context)


def about(request):
    title = "О нас"
    context = get_data(title=title)
    return render(request, 'about.html', context)


def contacts(request):
    title = "Связаться с нами"
    context = get_data(title=title)
    return render(request, 'contacts.html', context)


def product(request, pk):
    title = "Продукт"
    prod = Product.objects.get(pk=pk)
    context = get_data(title=title, prod=prod)
    return render(request, 'product.html', context)


def products(request):
    title = "Котолог продуктов"
    _products = Product.objects.all()
    context = get_data(title=title, prods=_products)
    return render(request, 'products.html', context)
