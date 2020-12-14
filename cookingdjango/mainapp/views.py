from django.shortcuts import render, redirect

from mainapp.models import SubjectCategory, Books, Personality, Document


def index(request):
    return render(request, 'mainapp/index.html')



def catalog(request):
    categories = SubjectCategory.objects.filter()
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

def personality(request):
    personality = Personality.objects.filter()
    context = {
        'personality': personality,
        'page_title': 'каталог личностей'
    }
    return render(request, 'mainapp/personality.html', context)


def book_page(request, book_pk):
    book = Books.objects.get(pk=book_pk)
    context = {
        'book': book,
        'page_title': 'страница книг'
    }
    return render(request, 'mainapp/book_page.html', context)


def personality_page(request, personality_pk):
    personalitys = Personality.objects.get(pk=personality_pk)
    context = {
        'personalitys': personalitys,
        'page_title': 'личности'
    }
    return render(request, 'mainapp/personality_page.html', context)

def document(request, document_pk):
    document = Document.objects.get(pk=document_pk)
    context = {
        'document': document,
        'page_title': 'документы'
    }
    return render(request, 'mainapp/document.html', context)


def model_form_upload(request):
    if request.method == 'POST':
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BooksForm()
    return render(request, 'mainapp/book_page.html', {
        'form': form
    })
