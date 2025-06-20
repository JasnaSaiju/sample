from rest_framework import serializers
from .models import Person
from .models import State,Dist

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dist
        fields='__all__'

class StateSerializer(serializers.ModelSerializer):
    districts=DistrictSerializer(many=True)
    class Meta:
        model=State
        fields='__all__'