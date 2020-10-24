from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView , DetailView
from .models import Property , PropertyImages , PropertyReview , Category



class PropertyList(ListView):
    model = Property



class PropertyDetail(DetailView):
    model = Property


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["property_images"] = PropertyImages.objects.filter(property=self.get_object().id)
        context['get_related'] = 
        return context
    


