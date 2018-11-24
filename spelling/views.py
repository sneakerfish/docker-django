from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from spelling.make_ngrams import lookup_word

# Create your views here.
def index(request):
    return HttpResponse("Hello, world.  You are at spelling index.")

def search(request):
    word_id = request.GET.get('lookup', '')
    lookup_results = []
    if word_id != '':
        lookup_results = lookup_word(word_id)
    context = {
        'lookup_results': lookup_results,
    }
    template = loader.get_template('spelling/index.html')
    return HttpResponse(template.render(context, request))
