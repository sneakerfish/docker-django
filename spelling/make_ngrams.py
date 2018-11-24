from spelling.models import Word, Ngram

def make_ngrams(word):
    newword = '*' + word.lower() + '*'
    return [newword[n:n+3] for n in range(len(newword)-2)]

def load_words(file):
    with open(file) as fp:
        line = fp.readline().rstrip().lower()
        cnt = 1
        while line:
            if cnt % 100 == 0:
                print(line)
            word = line
            w = Word.objects.create(spelling=word)
            Ngram.objects.bulk_create(
                [Ngram(word=w, text=ngram) for ngram in make_ngrams(word)]
                )
            line = fp.readline().rstrip().lower()
            cnt += 1

def lookup_word(word):
    lookup_ngrams = make_ngrams(word)
    result = []
    lookup_str = ", ".join(list(map(lambda x: "'" + x + "'", lookup_ngrams)))
    sel = """select distinct spelling_word.id, spelling_word.spelling,
      levenshtein(\'{word}\', spelling_word.spelling) as ld
      from spelling_ngram, spelling_word
      where spelling_ngram.word_id = spelling_word.id
      and spelling_ngram.text in ({lookup_str})
      order by ld """.format(word=word, lookup_str=lookup_str)
    cnt = 0
    for w in Ngram.objects.raw(sel):
        cnt += 1
        result.append([w.spelling, w.ld])
        if cnt >= 20: break
    return result
