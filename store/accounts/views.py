from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import action

from accounts.models import *
from accounts.serializers import *
from rest_framework.response import Response


from django.contrib.auth.models import User

# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UserViewSet(viewsets.ViewSet):

    queryset = User.objects.filter()
    serializer_class = EmployeeSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @action(detail=False, methods=['post'])
    def employee(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserLoginSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

