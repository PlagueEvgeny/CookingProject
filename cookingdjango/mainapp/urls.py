"""cookingdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
import mainapp.views as mainapp
from django.urls import path



app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.catalog, name='catalog'),
    path('personality/', mainapp.personality, name='personality'),
    path('personality/personalitys/<int:personality_pk>', mainapp.personality_page, name='personality_page'),
    path('document/<int:document_pk>', mainapp.document, name='document'),
    path('catalog/category/<int:category_pk>/', mainapp.catalog_section, name='catalog_section'),
    path('catalog/book/<int:book_pk>/', mainapp.book_page, name='book_page'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

