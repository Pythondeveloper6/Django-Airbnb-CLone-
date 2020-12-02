from django.urls import path
from .views import profile , profile_edit , signup , my_reservation , add_feedback


app_name = 'accounts'

urlpatterns = [
    path('signup',signup , name='signup'),
    path('profile/',profile,name='profile'),
    path('profile/edit', profile_edit , name='profile_edit') ,
    path('profile/booking', my_reservation , name='my_reservation') ,
    path('profile/booking/<slug:slug>/review', add_feedback , name='add_feedback') 
]
