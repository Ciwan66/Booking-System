from django.urls import path
from . import views
from accounts.forms import LoginForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.dashboard,name='users_dashboard'),
    path('register/',views.RegisterView.as_view(),name='users_register'),
    path('login/',views.CustomLoginView.as_view(redirect_authenticated_user=True,authentication_form=LoginForm),name='users_login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='apartment/index.html'),name='users_logout'),

]
