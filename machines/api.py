

from .models import CoffeeMachine
from .serializers import MachinesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def MachinesList(request):
    all_machine = CoffeeMachine.objects.all()
    data = MachinesSerializer(all_machine, many=True).data
    return Response({'data': data})