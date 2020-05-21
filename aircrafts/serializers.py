from rest_framework.serializers import ModelSerializer, SerializerMethodField
from aircrafts.models import Company, Aircraft
from reservations.models import Ticket, Location
from users.models import Passenger

#Ticket
class PassengerSerializer(ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'name', 'phone', 'email', 'weight']

#Company
class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']

#TypeAircraft
class LocationTicketSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']

class TicketSerializer(ModelSerializer):
    origin = LocationTicketSerializer()
    destination = LocationTicketSerializer()

    class Meta:
        model = Ticket
        fields = ['id', 'origin', 'destination', 'date']


class AircraftSerializer(ModelSerializer):
    ticket = TicketSerializer(source='ticket_set', many=True)

    class Meta:
        model = Aircraft
        fields = ['id', 'model', 'capacity', 'package_capacity', 'enrollment', 'ticket']

#CompanyDetail
class CompanyDetailSerializer(ModelSerializer):
    aircraft = AircraftSerializer(source='aircraft_set', many=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'aircraft']

class AircraftDetailSerializer(ModelSerializer):
    company = CompanySerializer()
    passenger = SerializerMethodField()

    class Meta:
        model = Aircraft
        fields = ['id', 'model', 'capacity', 'package_capacity', 'enrollment', 'company', 'passenger']

    def get_passenger(self, passenger):
        passenger = Ticket.objects.filter(aircraft__id=passenger.id)

        passengers = [ticket.passenger for ticket in passenger]

        return PassengerSerializer(instance=passengers, many=True).data
