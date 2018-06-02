import datetime

from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    # This defines how the object will be represented.
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Published date', help_text='Date on which the post was published')

    # This defines how the object will be represented.
    def __str__(self):
        return self.post_title

    # States if the blog post was published less than a day ago.
    def published_today(self):
        """Returns True if the blog post was published less than a day ago."""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
