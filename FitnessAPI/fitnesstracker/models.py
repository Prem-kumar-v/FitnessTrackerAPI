from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    age = models.IntegerField(default=0)
    height = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
    
class Workout(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    exercise_type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()  # in minutes
    calories_burned = models.PositiveIntegerField()
    date = models.DateField()
    
    
    def __str__(self):
        return f"{self.user.username} - {self.exercise_type} on {self.date}"
    
    
    
class Diet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    protein = models.CharField(max_length=100)
    fat = models.CharField(max_length=100)
    carbs = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.food_item} on {self.date}"

