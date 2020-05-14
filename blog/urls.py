from django.urls import path
from . import views

urlpatterns = [
    path('', views.example, name='exampl'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='blog-home'),
    path('contacti/', views.contacti, name='blog-contacti'),
]
