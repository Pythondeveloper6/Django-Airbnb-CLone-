import django_filters
from .models import Property




class PropertyFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.NumberFilter(lookup_expr='lt')
    class Meta:
        model = Property
        fields = ['title','place', 'category','price']