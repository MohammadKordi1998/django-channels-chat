from django.urls import path
from .views import UserView, AuthView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', UserView.as_view(), name='users'),
    path('auth/', AuthView.as_view(), name='auth-view'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
