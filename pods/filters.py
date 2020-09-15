import django_filters
from .models import CoffeePods

class PodsFilter(django_filters.FilterSet):
    class Meta:
        model = CoffeePods
        fields = '__all__'
        exclude = ['pods_title']