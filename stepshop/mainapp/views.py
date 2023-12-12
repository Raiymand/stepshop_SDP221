from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, Category


def get_data(**kawargs):
    links_menu = [
        {'link': 'index', 'name': 'Главное'},
        {'link': 'products:index', 'name': 'Продукты'},
        {'link': 'about', 'name': 'О нас'},
        {'link': 'contacts', 'name': 'Контакты'}
    ]

    categories = Category.objects.all()

    context = {'links_menu': links_menu, "categories": categories}
    context.update(**kawargs)
    return context


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def index(request):
    title = "главное"
    prods = Product.objects.all()
    selected_product = Product.objects.first()
    basket = get_basket(request.user)
    context = get_data(title=title, prods=prods, basket=basket, selected_product=selected_product)
    return render(request, 'index.html', context)


def about(request):
    title = "О нас"
    basket = get_basket(request.user)
    context = get_data(title=title, basket=basket)
    return render(request, 'about.html', context)


def contacts(request):
    title = "Связаться с нами"
    basket = get_basket(request.user)
    context = get_data(title=title, basket=basket)
    return render(request, 'contacts.html', context)


def product(request, pk):
    title = "Продукт"
    prod = Product.objects.get(pk=pk)
    same_prod = Product.objects.exclude(pk=pk) #filter(category=prod.category)
    basket = get_basket(request.user)

    context = get_data(title=title, prod=prod, basket=basket, same_prod=same_prod)
    return render(request, 'product.html', context)


def products(request, pk=None):
    title = "Каталог продуктов"
    _products = Product.objects.order_by('price')
    context = {}

    basket = get_basket(request.user)

    if pk is not None:
        category = get_object_or_404(Category, pk=pk)
        _products = Product.objects.filter(category__pk=pk).order_by('price')
        context = get_data(category=category)
        context['selected_category_name'] = category.name

    context = get_data(title=title, prods=_products, basket=basket, **context)
    return render(request, 'products.html', context)
