from basketapp.models import BooksBasket
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from mainapp.models import Books


@login_required
def index(request):
    items = BooksBasket.objects.filter(user=request.user)
    context = {
        'object_list': items,
    }

    return render(request, 'basketapp/basket.html', context)


@login_required
def add(request, book_id):
    book = Books.objects.get(pk=book_id)
    BooksBasket.objects.get_or_create(
        user=request.user,
        book=book
    )
    return HttpResponseRedirect(
        reverse('mainapp:catalog_section',
                kwargs={'category_pk': book.category_id})
    )


@login_required
def remove(request, book_basket_id):
    if request.is_ajax():
        item = BooksBasket.objects.get(id=book_basket_id)
        item.delete()
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return JsonResponse({'status': 'ok',
                             'book_basket_id': book_basket_id})