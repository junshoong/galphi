from django.views.generic import ListView
from bookmark.models import Bookmark


class BookmarkLV(ListView):
    model = Bookmark
    template_name = 'bookmark/bookmark_list.html'
    context_object_name = 'bookmark'
