from catalog.models import Author, BookInstance
from django.contrib import admin
from catalog import models
# Register your models here.


class InstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 2


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('genres', 'author')
    list_display = ('title', 'author', 'isbn', 'get_genres')
    inlines = [InstanceInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'summary', 'genres', 'author')
        }),
        ('Stuff', {
            'fields': ('isbn', )
        })
    )


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name', )


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language', )
    fields = ('language', )
