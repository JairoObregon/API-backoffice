from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields= ('__all__')

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields= ('__all__')