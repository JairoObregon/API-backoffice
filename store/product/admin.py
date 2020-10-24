from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Producto)
admin.site.register(Category)
admin.site.register(ImageOptional)
admin.site.register(Color)
admin.site.register(Stock)
