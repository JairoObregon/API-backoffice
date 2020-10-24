from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.user.username


class PasswordReset (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    entry_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    last_update = models.DateTimeField()
    reset_code = models.IntegerField()
    used = models.BooleanField()

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.user


class Client (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    phone_number =models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.user