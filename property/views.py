from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView , DetailView
from django.views.generic.edit import FormMixin
from .models import Property , PropertyImages , PropertyReview , Category
from .forms import PropertyBookForm



class PropertyList(ListView):
    model = Property



class PropertyDetail(FormMixin , DetailView):
    model = Property
    form_class = PropertyBookForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["property_images"] = PropertyImages.objects.filter(property=self.get_object().id)
        context['get_related'] = Property.objects.filter(category=self.get_object().category)[:2]

        print(context['get_related'])
        return context


    def post(self, request, *args, **kwargs):
        pass
    


