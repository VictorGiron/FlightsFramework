from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from aircrafts.models import Company, Aircraft
from aircrafts.serializers import CompanySerializer, CompanyDetailSerializer, AircraftSerializer, AircraftDetailSerializer

# Create your views here.

#Company
class ListCreateCompany(ListCreateAPIView):
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompanyDetailSerializer
        elif self.request.method == 'POST':
            return CompanySerializer

class RetrieveUpdateDestroyCompany(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompanyDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return CompanySerializer

#Aircraft
class ListCreateAircraft(ListCreateAPIView):
    queryset = Aircraft.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AircraftDetailSerializer
        elif self.request.method == 'POST':
            return AircraftSerializer

class RetrieveUpdateDestroyAircraft(RetrieveUpdateDestroyAPIView):
    queryset = Aircraft.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AircraftDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return AircraftSerializer

