from django.db import models

# Create your models here.

class Category (models.Model):
    created = models.DateField(auto_now_add=True)
    display = models.BooleanField(default=False)
    display_in_homeimage = models.BooleanField(default=False)
    image = models.ImageField(upload_to="imagenes/categoria", blank=True, null=True)
    modified = models.DateField(auto_now=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    slug =  models.SlugField(blank=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name



class Producto(models.Model):
    
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    code = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    description = models.TextField()
    display = models.BooleanField(default=False)
    display_in_home = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to="imagenes/producto", blank=True, null=True)
    modified = models.DateField(auto_now=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    offer_discount = models.PositiveIntegerField()
    order = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8,decimal_places=2,default=0.0)
    slug =  models.SlugField(blank=True)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name

class ImageOptional(models.Model):
    product = models.ForeignKey(Producto,on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="imagenes/ImagenOptional")
    modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'ImageOptional'
        verbose_name_plural = 'ImageOptionals'

    def __str__(self):
        return self.product.name

class Color (models.Model):
    created = models.DateField(auto_now_add=True)
    hex_code = models.CharField(max_length=100, blank=True, null=True)
    modified = models.DateField(auto_now=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.name

class Stock (models.Model):
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    product = models.ForeignKey(Producto,on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'

    def __str__(self):
        return "{}-{}-{}".format(self.product,self.color,self.quantity)