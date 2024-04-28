from django.urls import path
from . import views

urlpatterns = [
   path('',views.dashboard,name='users_dashboard'),
   path('register/',views.RegisterView.as_view(),name='users_register'),
]
