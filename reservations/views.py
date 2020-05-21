from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from reservations.models import Ticket, Location
from reservations.serializers import TicketSerializer, TicketDetailSerializer, LocationSerializer, LocationDetailSerializer

# Create your views here.

#Ticket
class ListCreateTicket(ListCreateAPIView):
    queryset = Ticket.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TicketDetailSerializer
        elif self.request.method == 'POST':
            return TicketSerializer

class RetrieveUpdateDestroyTicket(RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TicketDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return TicketSerializer

#Location
class ListCreateLocation(ListCreateAPIView):
    queryset = Location.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LocationDetailSerializer
        elif self.request.method == 'POST':
            return LocationSerializer

class RetrieveUpdateDestroyLocation(RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LocationDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return LocationSerializer