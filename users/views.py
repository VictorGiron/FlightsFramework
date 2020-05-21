from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from users.models import Passenger, Package
from users.serializers import PassengerSerializer, PassengerDetailSerializer, PackageSerializer, PackageDetailSerializer

# Create your views here.
#Passenger
class ListCreatePassenger(ListCreateAPIView):
    queryset = Passenger.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PassengerDetailSerializer
        elif self.request.method == 'POST':
            return PassengerSerializer

class RetrieveUpdateDestroyPassenger(RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PassengerDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return PassengerSerializer

#Package
class ListCreatePackage(ListCreateAPIView):
    queryset = Package.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PackageDetailSerializer
        elif self.request.method == 'POST':
            return PackageSerializer

class RetrieveUpdateDestroyPackage(RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PackageDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return PackageSerializer