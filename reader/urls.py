from django.urls import path
from .import views

urlpatterns = [
    path('', views.tech, name="tech-index"),
    path('s', views.single, name="tech-single"),
    path('a', views.article, name="article1"),
]