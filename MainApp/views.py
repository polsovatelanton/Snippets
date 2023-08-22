from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    snippets = Snippet.objects.all()
    count = Snippet.objects.all().count()
    context = {
        'snippets': snippets,
        'count': count
               }
    return render(request, 'pages/view_snippets.html', context)


def snippet_page(request, snippet_id):
    snippet = Snippet.objects.get(pk=snippet_id)
    context = {
        'snippet': snippet
               }
    return render(request, 'pages/view_snippet.html', context)