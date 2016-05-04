from django.contrib import admin
from .models import Author, Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Book Details", {"fields": ["title", "authors"]}),
        ("Review", {"fields": ["is_favorite", "review", "date_reviewed"]}),
    ]

    readonly_fields = ("date_reviewed",)

    # Since list_display cannot take manytomany field we use
    # list_author() created in models.py
    def book_authors(self, obj):
        return obj.list_authors()

    # Short description for display title in the admin
    book_authors.short_description = "Author(s)"

    list_display = (
        "title", "book_authors", "date_reviewed", "is_favorite",
    )
    # New list properties learnt
    list_editable = ("is_favorite",)
    list_display_links = ("title", "date_reviewed",)
    list_filter = ("is_favorite", "authors")
    # traverse authors name field using __
    search_fields = ("title", "authors__name",)

# Register your models here.
admin.site.register(Author)
# admin.site.register(Book, BookAdmin)
# @admin.register(Book) used as a shortcut to register
