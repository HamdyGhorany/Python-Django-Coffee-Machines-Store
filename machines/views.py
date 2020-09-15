from django.shortcuts import render, get_object_or_404
from .models import CoffeeMachine
from .filters import MachineFilter

# Create your views here.

def all_machines(request):
    all_machines = CoffeeMachine.objects.all()

    myfilter = MachineFilter(request.GET,queryset=all_machines)
    all_machines = myfilter.qs
    context = {
        'all_machines' : all_machines,
        'myfilter' : myfilter
    }
    return render(request, 'machines.html', context)

def home(request):

    return render(request, 'home.html')