from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post , Category
from taggit.models import Tag
# Create your views here.



class PostList(ListView):
    model = Post



class PostDetail(DetailView):
    model = Post



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] =  Tag.objects.all()
        context['categories'] = Category.objects.all()
        context['recent_posts'] = Post.objects.all()[:3]
        return context
    


