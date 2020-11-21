from django.urls import path
from . import views
from . import api_view


app_name = 'blog'


urlpatterns = [
    path( '',views.PostList.as_view() , name='post_list' ),
    path('<slug:slug>',views.PostDetail.as_view() , name='post_detail'),



    path('api/list' , api_view.post_list_api , name='post_list'),
    path('api/list/<int:id>' , api_view.post_detail , name='post_detail'),
    path('api/list/<str:query>' , api_view.post_search , name='post_search'),
]
