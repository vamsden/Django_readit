# from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
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
