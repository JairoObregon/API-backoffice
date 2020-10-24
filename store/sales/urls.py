from rest_framework import routers
from django.urls import path
from .views import *

urlpatterns = [
]

router = routers.DefaultRouter()
router.register('order', OrderViewSet)
router.register('package', PackageViewSet)
urlpatterns = router.urls