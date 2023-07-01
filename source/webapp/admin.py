from django.contrib import admin

from webapp.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created_at', 'updated_at', 'status']
    list_display_links = ['id', 'author']
    search_fields = ['author', 'description']
    fields = ['author', 'email', 'description', 'created_at', 'updated_at', 'status']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Book, BookAdmin)
