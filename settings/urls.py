from django.urls import path
from . import views
from . import api_view


app_name = 'settings'


urlpatterns = [
    path( '',views.home , name='home' ),    
    path( 'search',views.home_search , name='home_search' ),    
    path( 'about/',views.AboutView.as_view() , name='about' ),
    path( 'contact',views.contact , name='contact' ),
    path( 'dashboard/',views.dashboard , name='dashboard' ),

    path( 'about/api',api_view.about_api , name='about_api' ),
    path( 'about/api/faq',api_view.faq_api , name='faq_api' ),
    path( 'contact/api',api_view.contact_api , name='contact_api' ),
]
