from django.urls import path,include
from rest_framework.authtoken import views
from .views import EmployeeViewSet
from rest_framework import routers
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register('login', UserViewSet)
router.register('client', EmployeeViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    #path('token/',views.obtain_auth_token)
]

urlpatterns = router.urls


