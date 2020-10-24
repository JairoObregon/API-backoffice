from rest_framework import serializers
from .models import *

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields= ('__all__')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields= ('__all__')

class ImageOptionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageOptional
        fields= ('__all__')

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields= ('__all__')


class StockSerializer (serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('__all__')