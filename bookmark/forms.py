from django import forms
from bookmark.models import Bookmark


class BookmarkForm(forms.ModelForm):
    tags = forms.CharField(max_length=200)

    class Meta:
        model = Bookmark
        fields = ['title', 'link', ]

    def __init__(self, *args, **kwargs):
        super(BookmarkForm, self).__init__(*args, **kwargs)
