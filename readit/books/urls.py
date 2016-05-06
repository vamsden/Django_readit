from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_books, name='home'),
    url(r'^authors/', views.AuthorList.as_view(), name='authors'),
]
