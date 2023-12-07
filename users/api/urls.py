from django.urls import path
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import GetUserView, CreateUserView, ResetPasswordView


urlpatterns =[
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', GetUserView.as_view()),
    path('create/', CreateUserView.as_view()),
    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),
]