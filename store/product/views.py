from django.shortcuts import render
from rest_framework import viewsets
from product.models import *
from .serializers import *

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriaSerializer
    
    def get_queryset(self):
        queryset = Category.objects.all()
        slug  = self.request.query_params.get('slug')

        if slug:
            queryset = Category.objects.filter(slug=slug)
            
        return queryset
    

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        queryset = Producto.objects.all()
        categoria  = self.request.query_params.get('category')
        order  = self.request.query_params.get('order')

        if categoria:
            queryset = queryset.filter(category=categoria)

        if  order == 'decreciente':
            queryset = queryset.order_by('-price')

        if  order == 'creciente':
            queryset = queryset.order_by('price')

        return queryset
    


class ImageOptionalViewSet(viewsets.ModelViewSet):
    queryset = ImageOptional.objects.all()
    serializer_class = ImageOptionalSerializer

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

