from django.shortcuts import render
from django.http import HttpResponse
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
