from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from bookmark.models import Bookmark


def list_and_create(request):
    if request.method == 'POST':
        pass

    if isinstance(request.user, AnonymousUser):
        objects = None
    else:
        objects = Bookmark.objects.filter(writer=request.user)
    return render(request, 'bookmark/bookmark_list.html', {
        'bookmark': objects,
    })

