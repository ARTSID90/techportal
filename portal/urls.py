from django.urls import path
from .import views

urlpatterns = [
    path('', views.tech, name="tech-index"),
    path('c', views.contact, name="tech-contact"),
    path('g', views.gadget, name="gadget"),
    path('v', views.video, name="video"),
    path('s', views.single, name="tech-single"),
    path('a', views.article1, name="article 1"),
    path('2', views.article2, name="article 2"),
    path('a51', views.articlea51, name="article a51"),
    path('appoint', views.appointment, name="appointment"),
]