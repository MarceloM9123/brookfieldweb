from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=140)
    blog_image = models.ImageField(null=True, upload_to="blog/media")
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

