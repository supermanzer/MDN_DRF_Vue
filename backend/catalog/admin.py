from django.contrib import admin
from .models import Author, Genre, Book, BookInstance


# Inline classes
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


# Admin classes
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_title', 'status', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
# Genre is just a single name so no fancy admin for this one!
admin.site.register(Genre)
