from django.urls import path
from users import views

urlpatterns = [
    path('passenger/', views.ListCreatePassenger.as_view(), name='passengers'),
    path('passenger/<int:pk>/', views.RetrieveUpdateDestroyPassenger.as_view(), name='passenger'),

    path('package/', views.ListCreatePackage.as_view(), name='packages'),
    path('package/<int:pk>/', views.RetrieveUpdateDestroyPackage.as_view(), name='package'),
]
