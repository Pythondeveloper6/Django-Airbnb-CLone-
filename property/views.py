from django.shortcuts import redirect, render

# Create your views here.
from django.views.generic import ListView , DetailView
from django.views.generic.edit import FormMixin
from .models import Property , PropertyImages , PropertyReview , Category
from .forms import PropertyBookForm
from django.urls import reverse
from django.contrib import messages




class PropertyList(ListView):
    model = Property
    paginate_by = 1



class PropertyDetail(FormMixin , DetailView):
    model = Property
    form_class = PropertyBookForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["property_images"] = PropertyImages.objects.filter(property=self.get_object().id)
        context['get_related'] = Property.objects.filter(category=self.get_object().category)[:2]
        context['review_count'] = PropertyReview.objects.filter(property=self.get_object()).count()

        return context


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.save()
            messages.success(request, 'Your Reservation Confirmed ')

            ### send gmail message

            return redirect(reverse('property:property_detail' , kwargs={'slug':self.get_object().slug}))
    


