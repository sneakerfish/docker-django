from django.contrib import admin

# Register your models here.
from .models import Word, Ngram

admin.site.register(Word)
admin.site.register(Ngram)
