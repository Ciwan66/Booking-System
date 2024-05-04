from django.contrib import admin
from django.urls import path , include
from . import views



urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('<int:pk>/',views.ApartmentDetailView.as_view(),name='detail'),
    path('search/', views.search_apartments, name='search_apartments'),
    path('add-favorite/', views.FavoriteCreateView.as_view(), name='favorite_create'),
    path('delete-favorite/<int:pk>', views.FavoriteDeleteView.as_view(), name='favorite_delete'),

    path('comment/',include('reviews.urls')),

    
] 
  