from django.urls import path
from . import views

urlpatterns = [
    path('', views.featured, name='featured')

]