from django.shortcuts import render
from django.views.generic import ListView
from .models import FAQ , About , Info
from property import models as property_models
from blog import models as blog_models
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.core.mail import send_mail
from django.conf import settings
from .tasks import send_mail_task
# Create your views here.




def home(request):
    property_category = property_models.Category.objects.all()
    recent_posts = blog_models.Post.objects.all()[:4]
    popular_appartments = property_models.Property.objects.filter(category__name='Apparment')[:4]
    popular_villa = property_models.Property.objects.filter(category__name='Vella')[:5]
    popular_suits = property_models.Property.objects.filter(category__name='suite')[:5]
    about = About.objects.last()

    users_count = User.objects.all().count()
    appartments_count = property_models.Property.objects.filter(category__name='Apparment').count()
    villa_count = property_models.Property.objects.filter(category__name='Vella').count()
    suits_count = property_models.Property.objects.filter(category__name='suite').count()

    places = property_models.Place.objects.all().annotate(property_count=Count('property_place'))

    return render(request,'settings/index.html', {
        'property_category': property_category , 
        'recent_posts' : recent_posts , 
        'popular_appartments': popular_appartments , 
        'about':about  , 
        'popular_villa' : popular_villa , 
        'popular_suits' : popular_suits ,
        'users_count' : users_count , 
        'appartments_count': appartments_count , 
        'villa_count' : villa_count  , 
        'suits_count' : suits_count , 
        'places':places
    })



def home_search(request):
    name = request.GET.get('q','')
    location = request.GET['location']


    search_result = property_models.Property.objects.filter(
            Q(place__icontains=location) &
            Q(title__icontains=name) 
            # Q(description__icontains=name) 

    )

    return render(request,'settings/home_search.html',{'search_result': search_result})





class AboutView(ListView):
    model = FAQ


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.last() 
        return context
    




def contact(request):
    site_info = Info.objects.last()

    if request.method == 'POST':
        subject = request.POST['subject']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']


        send_mail_task.delay(subject , name,email,message)


    return render(request,'settings/contact.html',{'site_info': site_info})




def dashboard(request):
    
    users_count = User.objects.all().count()
    appartments_count = property_models.Property.objects.filter(category__name='Apparment').count()
    villa_count = property_models.Property.objects.filter(category__name='Vella').count()
    suits_count = property_models.Property.objects.filter(category__name='suite').count()
    posts = blog_models.Post.objects.all().count()
    booking = property_models.PropertyBook.objects.all().count()

    return render(request,'settings/dashboard.html',{
        'users_count' : users_count , 
        'appartments_count': appartments_count , 
        'villa_count' : villa_count  , 
        'suits_count' : suits_count ,  
        'posts_count' : posts , 
        'booking_count' : booking
    })