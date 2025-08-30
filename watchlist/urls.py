from django.urls import path
from . import views

urlpatterns = [
    path('watchlist/', views.user_watchlist, name='watchlist'),
    path('watchlist/add/', views.add_to_watchlist, name='add-to-watchlist'),
    path('watchlist/remove/', views.remove_from_watchlist, name='remove-from-watchlist'),
]