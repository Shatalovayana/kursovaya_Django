from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'body', 'image', 'created_at', 'views_count',)
    search_fields = ('title',)