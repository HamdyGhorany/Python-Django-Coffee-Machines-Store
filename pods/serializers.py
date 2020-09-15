from rest_framework import serializers
from .models import CoffeePods


class PodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeePods
        fields = '__all__'