from django.shortcuts import render, get_object_or_404
from .models import CoffeePods
from .filters import PodsFilter

# Create your views here.


def all_pods(request):
    all_pods = CoffeePods.objects.all()

    myfilter = PodsFilter(request.GET,queryset=all_pods)
    all_pods = myfilter.qs
    context = {
        'all_pods' : all_pods,
        'myfilter' : myfilter
    }
    return render(request, 'pods.html', context)