from rest_framework.serializers import ModelSerializer, SerializerMethodField, HyperlinkedModelSerializer
from reservations.models import Location, Ticket
from users.models import Passenger, Package
from aircrafts.models import Aircraft

#UsersSerializers
class AircraftSerializer(ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ['id', 'model', 'enrollment', 'company']

class PackageSerializer(ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'weight', 'color', 'brand']

class PassengerSerializer(ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'name', 'phone']

class TicketLocationSerializer(ModelSerializer):
    passenger = PassengerSerializer()
    package = PackageSerializer(many=True)

    class Meta:
        model = Ticket
        fields = ['id', 'passenger', 'package', 'date']

#Location
class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']

class LocationTicketSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']

#Ticket
class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'passenger', 'package', 'aircraft', 'origin', 'destination', 'date']

#DetailSerializers
class TicketDetailSerializer(ModelSerializer):
    package = PackageSerializer(many=True)
    passenger = PassengerSerializer()
    aircraft = AircraftSerializer()
    origin = LocationTicketSerializer()
    destination = LocationTicketSerializer()

    class Meta:
        model = Ticket
        fields = ['id', 'passenger', 'package', 'aircraft', 'origin', 'destination', 'date']

class LocationDetailSerializer(HyperlinkedModelSerializer):
    ticket = TicketLocationSerializer(source='destination', many=True)

    class Meta:
        model = Location
        fields = ['id', 'name', 'ticket']

