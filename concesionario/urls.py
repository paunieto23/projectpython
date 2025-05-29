from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.car_list, name='cars-list'),
    path('cars/<slug:slug>/', views.car_detail, name='cars-detail'),
    path('dealers/', views.dealer_list, name='dealers-list'),
    path('dealers/<slug:slug>/', views.dealer_detail, name='dealers-detail'),
    path('tags/', views.tag_list, name='tags-list'),
    path('tags/<slug:slug>/', views.tag_car_list, name='tag-cars'),
]
