from django.db import models

# Create your models here.
class Passenger(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    dpi = models.IntegerField()
    weight = models.CharField(max_length=20)

    def __str__(self):
        return self.name + '(' + self.weight + ')'


class Package(models.Model):
    weight = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    brand = models.CharField(max_length=30)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand + ', ' + self.color + '(' + self.weight + ')'
