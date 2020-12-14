from django.contrib import admin

from mainapp.models import SubjectCategory, Books, Personality, Document

admin.site.register(SubjectCategory)
admin.site.register(Books)
admin.site.register(Personality)
admin.site.register(Document)
