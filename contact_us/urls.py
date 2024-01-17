from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import ContactUsView


router = DefaultRouter()
router.register('', ContactUsView)

urlpatterns = [
    path('', include(router.urls))
]
