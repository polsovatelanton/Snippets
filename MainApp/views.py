from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
from MainApp.forms import SnippetdelForm

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'pages/add_snippet.html', context)

    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets-list")
        return render(request, 'pages/add_snippet.html', {'form': form})


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

def snippet_dell(request, snippet_id):
    Snippet.objects.filter(id=snippet_id).delete()
    return redirect("snippets-list")

#def create_snippet(request):
#   if request.method == "POST":
#       form = SnippetForm(request.POST)
#       if form.is_valid():
#           form.save()
#           return redirect("snippets-list")
#       return render(request,'add_snippet.html', {'form': form})