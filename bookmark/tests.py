from django.test import TestCase
from django.contrib.auth import get_user_model
from bookmark.models import Bookmark, Tag


class BookmarkModelTest(TestCase):

    @staticmethod
    def _create_user():
        user = get_user_model().objects.create(username='test')
        user.set_password('test')
        user.save()
        return user

    def test_create_Bookmark(self):
        user = self._create_user()
        first_bookmark = Bookmark()
        first_bookmark.title = '구글'
        first_bookmark.link = 'https://www.google.co.kr'
        first_bookmark.writer = user
        first_bookmark.save()
        first_tag = Tag(name='portal')
        first_tag.save()
        second_tag = Tag(name='search')
        second_tag.save()
        first_bookmark.tag.add(first_tag, second_tag)

        saved_bookmark = Bookmark.objects.all()
        self.assertEqual(saved_bookmark.count(), 1)
        self.assertEqual(saved_bookmark[0].tag.all()[0], first_tag)
        self.assertEqual(saved_bookmark[0].tag.all()[1], second_tag)
        self.assertEqual(saved_bookmark[0].title, '구글')



