from django import forms
from uploads.core.models import Books

class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('name', 'books', )