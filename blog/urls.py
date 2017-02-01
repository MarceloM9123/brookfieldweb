from django.conf.urls import url
from blog.views import BlogPosts
from blog.models import Post


urlpatterns = [url(r'^$', BlogPosts.as_view(model = Post, template_name = 'blog/blog.html'))]

