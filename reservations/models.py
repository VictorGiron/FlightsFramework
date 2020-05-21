from django.db import models
from users.models import Passenger, Package
from aircrafts.models import Aircraft

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    package = models.ManyToManyField(Package)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    origin = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='origin')
    destination = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='destination')
    date = models.DateTimeField()

    def __str__(self):
        return self.passenger.name + ', ' + self.aircraft.model + '(' + str(self.date) + ')'
