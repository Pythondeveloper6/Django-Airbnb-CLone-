from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post , Category
from taggit.models import Tag
from django.db.models import Count, Q
# Create your views here.



class PostList(ListView):
    model = Post
    paginate_by = 8


    def get_queryset(self):
        name = self.request.GET.get('q','')
        
        object_list = Post.objects.filter(
            Q(title__icontains=name) | 
            Q(description__icontains=name)
        )
        return object_list
    


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] =  Tag.objects.all()
        context['categories'] = Category.objects.all().annotate(post_count=Count('post_category'))
        context['recent_posts'] = Post.objects.all()[:3]
        return context
    


class PostsByCategory(ListView):
    model = Post

    def get_queryset(self):
        objects_list = Post.objects.filter(
            Q(category__name__icontains=self.kwargs['slug'])
        )
        return objects_list
    


class PostsByTags(ListView):
    model = Post

    def get_queryset(self):
        objects_list = Post.objects.filter(
            Q(tags__name__icontains=self.kwargs['slug'])
        )
        return objects_list