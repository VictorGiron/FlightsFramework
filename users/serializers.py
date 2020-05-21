from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.models import Passenger, Package
from reservations.models import Ticket, Location
from aircrafts.models import Aircraft

#ReservationsSerializers
class PackagePassengerSerializer(ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'weight', 'color', 'brand']

class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']
class AircraftSerializer(ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ['id', 'model', 'company']

class TicketSerializer(ModelSerializer):
    origin = LocationSerializer()
    destination = LocationSerializer()
    aircraft = AircraftSerializer()

    class Meta:
        model = Ticket
        fields = ['aircraft', 'origin', 'destination', 'date']

#Package
class PackageSerializer(ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'weight', 'color', 'brand', 'passenger']


#Passenger
class PassengerSerializer(ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'name', 'weight', 'phone', 'email', 'dpi']

#DetailSerializers
class PackageDetailSerializer(ModelSerializer):
    passenger = PassengerSerializer()

    class Meta:
        model = Package
        fields = ['id', 'weight', 'color', 'brand', 'passenger']

class PassengerDetailSerializer(ModelSerializer):
    package = PackagePassengerSerializer(source='package_set', many=True)
    ticket = TicketSerializer(source='ticket_set', many=True)

    class Meta:
        model = Passenger
        fields = ['id', 'name', 'weight', 'package', 'ticket']
