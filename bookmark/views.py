from django.views.generic import ListView
from django.contrib.auth.models import AnonymousUser
from bookmark.models import Bookmark


class BookmarkLV(ListView):
    model = Bookmark
    template_name = 'bookmark/bookmark_list.html'
    context_object_name = 'bookmark'

    def get_queryset(self):
        if isinstance(self.request.user, AnonymousUser):
            return
        return Bookmark.objects.filter(writer=self.request.user)
