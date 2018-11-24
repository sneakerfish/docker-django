from django.db import models

# Create your models here.
class Word(models.Model):
    spelling = models.CharField(max_length=50)

    @property
    def ngrams(word):
        newword = '*' + word.lower() + '*'
        return [newword[n:n+3] for n in range(len(newword)-2)]

class Ngram(models.Model):
    text = models.CharField(max_length=3)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
