from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from bookmark.models import Bookmark
from bookmark.models import Tag
from bookmark.forms import BookmarkForm


def list_and_create(request):
    form = BookmarkForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        tag_list = []
        tags = form.cleaned_data['tags'].split(',')
        for tag in tags:
            t, created = Tag.objects.get_or_create(name=tag)
            tag_list.append(t)
        bookmark = form.save(commit=False)
        bookmark.writer = request.user
        bookmark.save()
        bookmark.tag.add(*tag_list)

    if isinstance(request.user, AnonymousUser):
        objects = None
    else:
        objects = Bookmark.objects.filter(writer=request.user)
    return render(request, 'bookmark/index.html', {
        'bookmark': objects, 'form': form,
    })

