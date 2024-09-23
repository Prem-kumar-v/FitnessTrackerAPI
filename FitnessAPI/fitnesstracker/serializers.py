from rest_framework import serializers
from .models import User,Workout,Diet

class user_serializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = User
        fields = ['id','username','email','age','height','weight','contact_no']
        
class Workout_serializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Workout
        fields = '__all__'
        
class Diet_serializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Diet
        fields = '__all__'