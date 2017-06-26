from django.conf.urls import url
from bookmark.views import list_and_create

urlpatterns = [
    url(r'^$', list_and_create, name='bookmark_list'),
]
