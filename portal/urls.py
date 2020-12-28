from django.urls import path
from .import views

urlpatterns = [
    path('', views.tech, name="tech-index"),
    path('c', views.contact, name="tech-contact"),
    path('g', views.gadget, name="gadget"),
]