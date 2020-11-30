from django.urls import path
from . import views
from . import api_view


app_name = 'settings'


urlpatterns = [
    path( '',views.home , name='home' ),    
    path( 'about/',views.AboutView.as_view() , name='about' ),

    path( 'about/api',api_view.about_api , name='about_api' ),
    path( 'about/api/faq',api_view.faq_api , name='faq_api' ),
]
