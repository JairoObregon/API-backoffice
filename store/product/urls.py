
from rest_framework import routers
from django.urls import path
from product.views import *

urlpatterns = [
]

router = routers.DefaultRouter()
router.register('product', ProductoViewSet)
router.register('category', CategoryViewSet)
router.register('imageOptional', ImageOptionalViewSet)
router.register('color', ColorViewSet)
router.register('stock', StockViewSet)
urlpatterns = router.urls

