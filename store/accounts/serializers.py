from rest_framework import serializers
from .models import *
from django.contrib.auth import password_validation, authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Employee



class EmployeeSerializer(serializers.ModelSerializer):
    created = serializers.DateField(format='iso-8601', input_formats=None)
    modified = serializers.DateField(format='iso-8601', input_formats=None)
    
    class Meta:
        model =  Employee
        fields = ('__all__')
        
    
    """
    def create(self, validated_data):
           user = User.objects.create(
               username=validated_data['username'],
               email=validated_data['email'],
               first_name=validated_data['first_name'],
               last_name=validated_data['last_name']
           )
           created=validated_data['created']
           modified= validated_data['modified']

           user.set_password(validated_data['password'])
           user.save()
           Employee.objects.create(user=user,created=created,modified=modified)

           return user
    """


class UserLoginSerializer(serializers.Serializer):

    # Campos que vamos a requerir
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=64)

    # Primero validamos los datos
    def validate(self, data):

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


