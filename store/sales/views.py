from django.shortcuts import render
from rest_framework import viewsets
from product.models import *
from .serializers import *

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()
        state  = self.request.query_params.get('state')
        if state:
            queryset = Order.objects.filter(state=state)
            
        return queryset


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
