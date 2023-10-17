from django.shortcuts import render


def index(request):
    title = "главное"
    links_menu = [
        {'link': 'index', 'name': 'Главное'},
        {'link': 'products:index', 'name': 'Продукты'},
        {'link': 'about', 'name': 'О нас'},
        {'link': 'contacts', 'name': 'Контакты'}
    ]
    context = {'title': title, 'links_menu': links_menu}

    return render(request, 'index.html', context)


def about(request):
    title = "О нас"
    context = {'title': title}

    return render(request, 'about.html', context)


def contacts(request):
    title = "Связаться с нами"
    context = {'title': title}

    return render(request, 'contacts.html', context)


def product(request):
    title = "Продукт"
    context = {'title': title}

    return render(request, 'product.html', context)


def products(request):
    title = "Котолог продуктов"
    context = {'title': title}

    return render(request, 'products.html', context)
