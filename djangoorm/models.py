from django.db import models

class Word(models.Model):
    spelling = models.CharField(max_length=20)

class Ngram(models.Model):
    text = models.CharField(max_length=3)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
