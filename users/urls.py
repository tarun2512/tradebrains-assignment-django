from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),  # ✅ Built-in JWT login
]