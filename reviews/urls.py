from django.urls import path
from . import views

urlpatterns = [
    path('comment',views.CommentAdd.as_view(),name='comment')
]
