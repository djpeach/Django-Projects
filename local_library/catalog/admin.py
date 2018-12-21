from django.contrib import admin
from . import models

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


class BookInlines(admin.TabularInline):
    model = models.Book
    extra = 1


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields=['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInlines]


class BookInstanceInlines(admin.TabularInline):
    model = models.BookInstance
    extra = 1


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'display_genre')
    inlines=[BookInstanceInlines]


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display=('display_book_title', 'status', 'due_back', 'id')
    list_filter=('status', 'due_back')
    fieldsets=(
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )
    readonly_fields = ['id']
