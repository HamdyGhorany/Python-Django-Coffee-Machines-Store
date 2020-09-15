import django_filters
from .models import CoffeeMachine

class MachineFilter(django_filters.FilterSet):
    class Meta:
        model = CoffeeMachine
        fields = ['product_type', 'Category']
        #exclude = ['product_title', 'water_line_compatible']