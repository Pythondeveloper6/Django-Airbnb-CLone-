from django.shortcuts import render
from django.views.generic import ListView
from .models import FAQ , About
from property import models as property_models
from blog import models as blog_models
# Create your views here.




def home(request):
    property_category = property_models.Category.objects.all()
    recent_posts = blog_models.Post.objects.all()[:4]
    popular_appartments = property_models.Property.objects.filter(category__name='Apparment')[:4]
    about = About.objects.last()
    return render(request,'settings/index.html', {
        'property_category': property_category , 
        'recent_posts' : recent_posts , 
        'popular_appartments': popular_appartments , 
        'about':about 
    })




class AboutView(ListView):
    model = FAQ


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.last() 
        return context
    

