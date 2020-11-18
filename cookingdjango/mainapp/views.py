from django.shortcuts import render

from mainapp.models import SubjectCategory, Books


def index(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    categories = SubjectCategory.objects.all()
    context = {
        'categories': categories,
        'page_title': 'каталог'
    }

    return render(request, 'mainapp/catalog.html', context)

def catalog_section(request, category_pk):
    books = Books.objects.filter(category_id=category_pk)
    context = {
        'books': books,
        'page_title': 'страница каталога'
    }
    return render(request, 'mainapp/catalog_page.html', context)


def book_page(request, book_pk):
    book = Books.objects.get(pk=book_pk)
    context = {
        'book': book,
        'page_title': 'страница книг'
    }
    return render(request, 'mainapp/book_page.html', context)
