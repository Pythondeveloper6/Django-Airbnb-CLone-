from django.urls import path
from . import views
from . import api_view


app_name = 'property'


urlpatterns = [
    path( '',views.PropertyList.as_view() , name='property_list' ),
    path( 'new',views.NewProperty.as_view() , name='property_new' ),
    path('<slug:slug>',views.PropertyDetail.as_view() , name='property_detail'),


    path('api/list' , api_view.PropertyListApi.as_view(), name='property_list'),
    path('api/list/<int:pk>' , api_view.PropertyDetailApi.as_view(), name='property_detail')
]
