
from django.urls import path, include
from django.db import router
from rest_framework.routers import DefaultRouter


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api.views import UserViewSet
from . import views

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')



urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', views.UserCreateAPIView.as_view(), name='user_create'),
    path('user/', views.ListUserAPIView.as_view(), name='user_create'),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]