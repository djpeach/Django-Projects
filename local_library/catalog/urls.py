from django.urls import path
from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='book-list-view'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail-view'),
    path('authors/', views.AuthorListView.as_view(), name='author-list-view'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail-view'),
]
