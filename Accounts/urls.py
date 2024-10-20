from django.contrib import admin
from django.urls import path
from .views import UserCreate, UserProfileDetail, ChangePasswordUser,\
    PasswordResetRequestView, PasswordResetConfirmView, UserLogoutViews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
app_name = 'accounts'


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('create/user/', UserCreate.as_view(), name='create_user'),
    path('profile/', UserProfileDetail.as_view(), name='user_profile'),
    path('change/password/', ChangePasswordUser.as_view(), name='user_change_password'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset-req'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-rest-confirm'),
    path('user/logout/', UserLogoutViews.as_view(), name='user_logout'),
]