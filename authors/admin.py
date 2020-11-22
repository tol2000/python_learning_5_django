from django.contrib import admin

from authors.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'full_name', 'level', 'email')
    list_display_links = ('id', 'first_name', 'last_name', 'level')
    # sortable_by = ('id', 'email')

    @staticmethod
    def full_name(obj):
        return f'{obj.first_name} {obj.last_name}'
