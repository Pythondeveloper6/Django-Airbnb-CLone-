from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView , DetailView
from .models import Property , PropertyImages , PropertyReview , Category



class PropertyList(ListView):
    model = Property



class PropertyDetail(DetailView):
    model = Property


