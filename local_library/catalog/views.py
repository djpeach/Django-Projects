from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import models


def index(req):
    hm_books = models.Book.objects.all().count()
    hm_instances = models.BookInstance.objects.all().count()
    hm_authors = models.Author.objects.all().count()

    hm_instances_available = models.BookInstance.objects.filter(status__exact='a').count()

    context = {
        'hm_books': hm_books,
        'hm_instances': hm_instances,
        'hm_authors': hm_authors,
        'hm_instances_available': hm_instances_available,
    }

    return render(req, 'index.html', context=context)


class BookListView(generic.ListView):
    model = models.Book
    extra_context = {
        'model_object': 'book',
    }


class BookDetailView(generic.DetailView):
    model = models.Book


class AuthorListView(generic.ListView):
    model = models.Author
    extra_context = {
        'model_object': 'author',
    }


class AuthorDetailView(generic.DetailView):
    model = models.Author
