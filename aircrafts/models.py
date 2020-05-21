from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Aircraft(models.Model):
    model = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50)
    package_capacity = models.CharField(max_length=50)
    enrollment = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.model + '(' + ', ' + self.enrollment + ')'
