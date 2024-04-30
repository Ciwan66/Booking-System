from django.urls import path
from . import views
from accounts.forms import LoginForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.dashboard,name='users_dashboard'),
    path('register/',views.RegisterView.as_view(),name='users_register'),
    path('login/',views.CustomLoginView.as_view(redirect_authenticated_user=True,authentication_form=LoginForm),name='users_login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='apartment/list.html'),name='users_logout'),
     path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        views.activate, name='activate'),
]
