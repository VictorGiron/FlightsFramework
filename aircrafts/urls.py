from django.urls import path
from aircrafts import views

urlpatterns = [
    path('company/', views.ListCreateCompany.as_view(), name='Companies'),
    path('company/<int:pk>/', views.RetrieveUpdateDestroyCompany.as_view(), name='Company'),

    path('aircraft/', views.ListCreateAircraft.as_view(), name='aircrafts'),
    path('aircraft/<int:pk>/', views.RetrieveUpdateDestroyAircraft.as_view(), name='aircraft'),
]