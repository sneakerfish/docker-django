from models import Word, Ngram
import django_filters

class WordFilter(django_filters.FilterSet):
    class Meta:
        model = Word
        fields = ["spelling"]
