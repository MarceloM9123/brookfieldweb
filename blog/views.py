from django.views.generic.list import ListView
from blog.models import Post


class BlogPosts(ListView):

    model = Post
    paginate_by = 2

