from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PatientViewSet, UserregistrationApiView,activate, UserLoginAPIView, UserLogoutAPIView

router = DefaultRouter()
router.register('list', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserregistrationApiView.as_view(), name= 'register'),
    path('login/', UserLoginAPIView.as_view(), name= 'login'),
    path('logout/', UserLogoutAPIView.as_view(), name= 'logout'),
    path('active/<uid64>/<token>/', activate, name= 'active'),
]