from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post , Category
from taggit.models import Tag
from django.db.models import Count
# Create your views here.



class PostList(ListView):
    model = Post
    paginate_by = 8


    def get_queryset(self):
        name = self.kwargs.get('name','')
        return super().get_queryset()
    


class PostDetail(DetailView):
    model = Post



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] =  Tag.objects.all()
        context['categories'] = Category.objects.all().annotate(post_count=Count('post_category'))
        context['recent_posts'] = Post.objects.all()[:3]
        return context
    


