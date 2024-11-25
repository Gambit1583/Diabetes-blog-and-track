from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Specialist(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason_for_visit = models.TextField()

    def __str__(self):
        return f"Appointment with {self.specialist.name} on {self.date}"
