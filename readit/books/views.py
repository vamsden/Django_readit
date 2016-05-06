# from django.http import HttpResponse
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import View
from .models import Author, Book
# Create your views here.


def list_books(request):
    # return HttpResponse(request.user.username)
    """
    List the books thats have review
    """

    books = Book.objects.exclude(
        date_reviewed__isnull=True).prefetch_related('authors')

    context = {
        'books': books,
    }
    return render(request, 'books/list.html', context)

# class based view


class AuthorList(View):
    def get(self, request):

        # Filters out authors with books == 0
        # Count method is imported--> from django.db.models import Count
        authors = Author.objects.annotate(
            published_books=Count('books')
        ).filter(
            published_books__gt=0
        )

        context = {
            'authors': authors,
        }
        return render(request, "books/authors.html", context)
