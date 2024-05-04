from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:aprt>',views.CommentAdd.as_view(),name='comment')
]
