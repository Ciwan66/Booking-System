from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('',views.ApartmentListView.as_view(),name='index'),
    path('<int:pk>',views.ApartmentDetailView.as_view(),name='detail'),
    path('search/', views.search_apartments, name='search_apartments'),

    
] 
  