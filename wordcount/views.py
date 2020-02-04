from django.http import HttpResponse
from django.shortcuts import render
import operator

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext) 
    words = fulltext.split(' ')
    worddictionary = {}

    for word in words:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word] =1 

    sortedwords =sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'fulltext':fulltext, 'len': len(words), 'worddictionary':sortedwords})