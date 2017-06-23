from django.db import models
from django.contrib.auth import get_user_model


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Bookmark(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.title, self.link)



