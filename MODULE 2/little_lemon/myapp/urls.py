from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  # Maps to the home view
    path('aboutus/', views.about, name="about"),  # Changed path
    path('menu/', views.menu, name="menu"),  # Menu page
    path('book/', views.book, name="book"),  # Booking page
]