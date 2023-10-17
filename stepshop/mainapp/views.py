from django.shortcuts import render


def create_context(title):
    links_menu = [
        {'link': 'index', 'name': 'Главное'},
        {'link': 'products:index', 'name': 'Продукты'},
        {'link': 'about', 'name': 'О нас'},
        {'link': 'contacts', 'name': 'Контакты'}
    ]
    context = {'title': title, 'links_menu': links_menu}
    return context


def index(request):
    title = "главное"
    context = create_context(title)
    return render(request, 'index.html', context)


def about(request):
    title = "О нас"
    context = create_context(title)
    return render(request, 'about.html', context)


def contacts(request):
    title = "Связаться с нами"
    context = create_context(title)
    return render(request, 'contacts.html', context)


def product(request):
    title = "Продукт"
    context = create_context(title)
    return render(request, 'product.html', context)


def products(request):
    title = "Котолог продуктов"
    context = create_context(title)
    return render(request, 'products.html', context)
