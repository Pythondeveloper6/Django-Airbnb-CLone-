from . models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q


@api_view(['GET'])
def post_list_api(request):
    all_posts = Post.objects.all()
    data = PostSerializer(all_posts , many=True).data
    return Response({'Success':True , 'Post List' : data})


@api_view(['GET'])
def post_detail(request,id):
    post = Post.objects.get(id=id)
    data = PostSerializer(post).data
    return Response({'Success': True , 'Post Detail' : data, 'Code' : 200})


@api_view(['GET'])
def post_search(request,query):
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    print(posts)
    data = PostSerializer(posts , many=True).data
    return Response({'Success':True , 'Post Search Results' : data})

