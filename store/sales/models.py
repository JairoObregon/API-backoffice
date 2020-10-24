from django.db import models
from product.models import Color,Producto
# Create your models here.



class Order(models.Model):
    
    address = models.CharField(max_length=100, blank=True, null=True)
    city =models.CharField(max_length=100, blank=True, null=True)
    created =  models.DateField(auto_now_add=True)
    district =models.CharField(max_length=100, blank=True, null=True)
    dni =models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    first_name=models.CharField(max_length=100, blank=True, null=True)
    last_name=models.CharField(max_length=100, blank=True, null=True)
    modified = models.DateField(auto_now=True)
    payme = models.BooleanField(default=False)
    phone_number =models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)
    purcharse_operation_number = models.CharField(max_length=100, blank=True, null=True)
    shipping = models.PositiveIntegerField(default=0)
    state =models.PositiveIntegerField(default=0)
    term_and_conditions = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.first_name

class Package(models.Model):
    
    color = models.ForeignKey('product.Color', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Producto', on_delete=models.CASCADE)
    quantity =  models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Package'
        verbose_name_plural = 'Packages'

    def __str__(self):
        return "{}-{}-{}".format(self.color,self.order,self.product)