

from .models import CoffeePods
from .serializers import PodsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def PodsList(request):
    all_machine = CoffeePods.objects.all()
    data = PodsSerializer(all_machine, many=True).data
    return Response({'data': data})