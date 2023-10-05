from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.multiply_by_ten),
]