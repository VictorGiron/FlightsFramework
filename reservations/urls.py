from django.urls import path
from reservations import views

urlpatterns = [
    path('ticket/', views.ListCreateTicket.as_view(), name='tickets'),
    path('ticket/<int:pk>/', views.RetrieveUpdateDestroyTicket.as_view(), name='ticket'),

    path('location/', views.ListCreateLocation.as_view(), name='locations'),
    path('location/<int:pk>/', views.RetrieveUpdateDestroyLocation.as_view(), name='location'),
]