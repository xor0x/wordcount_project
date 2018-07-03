from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    text = request.GET['text']
    wordlist = text.split()

    worddictinary = {}

    for word in wordlist:
        if word in worddictinary:
            worddictinary[word] += 1
        else:
            worddictinary[word] = 1

    sortedWords = sorted(worddictinary.items(), key = operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'text': text, 'count': len(wordlist), 'sortedwords': sortedWords})

def about(request):

    return render(request, 'about.html')
