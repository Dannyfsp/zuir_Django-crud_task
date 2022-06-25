from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic import ListView

from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = [
        “__all__”,
    ]
    success_url  = 'reverse_lazy(“blog:all”)'

class PostDetailView(DetailView):
    
