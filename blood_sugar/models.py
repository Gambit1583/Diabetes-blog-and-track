from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BloodSugarRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    blood_sugar_level = models.FloatField()
    carbohydrates_eaten = models.FloatField()

    def __str__(self):
        return f"Record for{self.user.username} on {self.date}"