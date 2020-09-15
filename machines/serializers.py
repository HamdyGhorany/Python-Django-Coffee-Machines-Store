from rest_framework import serializers
from .models import CoffeeMachine


class MachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMachine
        fields = '__all__'