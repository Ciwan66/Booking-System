from django.urls import path
from . import views
from accounts.forms import LoginForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.dashboard,name='users_dashboard'),
    path('register/',views.RegisterView.as_view(),name='users_register'),
    path('login/',views.CustomLoginView.as_view(redirect_authenticated_user=True,authentication_form=LoginForm),name='users_login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='apartment/list.html'),name='users_logout'),
    path('activate/<uidb64>/<token>/',  
        views.activate, name='activate'),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    
]
