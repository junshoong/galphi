from django.conf.urls import url
from bookmark.views import BookmarkLV

urlpatterns = [
    url(r'^$', BookmarkLV.as_view(), name='bookmark_list'),
]
