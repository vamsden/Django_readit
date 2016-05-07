from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_books, name='home'),
    url(r'^authors/', views.AuthorList.as_view(), name='authors'),
    url(r'^books/(?P<pk>[-\w]+)/$',
        views.BookDetail.as_view(), name='book-detail'),
    url(r'^author/(?P<pk>[-\w]+)/$',
        views.AuthorDetail.as_view(), name='author-detail'),
]
