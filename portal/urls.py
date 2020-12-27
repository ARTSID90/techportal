from django.urls import path
from .import views

urlpatterns = [
    path('', views.tech, name="tech-index"),
]