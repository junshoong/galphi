from django.contrib import admin
from bookmark.models import Bookmark, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'writer',)

admin.site.register(Tag, TagAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
