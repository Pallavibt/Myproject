from django.urls import path
from . import views

urlpatterns = [
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),  # Ensure this path is correct
]