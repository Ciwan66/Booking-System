from django.urls import path 
from .views import ReservationCreateView as ReservationCreateView
from .views import ReservationListView  as ReservationListView
from .views import ReservationDetailView  as ReservationDetailView
from .views import ReservationUpdateView  as ReservationUpdateView

urlpatterns = [
    path("", ReservationListView.as_view(), name='list-reserv'),
    path("res-details/<int:pk>", ReservationDetailView.as_view(), name='detail-reserv'),
    path("res-update/<int:pk>", ReservationUpdateView.as_view(), name='update-reserv'),
    path('take-house/<int:id>',ReservationCreateView.as_view(),name='creat-reserv'),
]
 