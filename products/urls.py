from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.painting_detail, name='painting_detail'),
    path('products/<genre_slug>/', views.genre, name='genre'),
    path('products/products/impressionism', views.impressionism, name='impressionism'),
]