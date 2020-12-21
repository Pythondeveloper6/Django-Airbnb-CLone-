from django.urls import path
from . import views
from . import api_view


app_name = 'blog'


urlpatterns = [
    path( '',views.PostList.as_view() , name='post_list' ),
    path('<slug:slug>',views.PostDetail.as_view() , name='post_detail'),
    
    path('category/<slug:slug>',views.PostsByCategory.as_view() , name='post_by_category'),
    path('tag/<slug:slug>',views.PostsByTags.as_view() , name='post_by_tag'),



    path('api/list' , api_view.post_list_api , name='post_list_api'),
    path('api/list/<int:id>' , api_view.post_detail , name='post_detail_api'),
    path('api/list/<str:query>' , api_view.post_search , name='post_search_api'),
]
