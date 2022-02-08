from rest_framework import serializers
from .models import *

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username' , 'email' , 'password']

    # velidation 
    def validate(self, data):

        if len(data["username"]) < 3 or len(data["username"]) > 50:
            raise serializers.ValidationError("Enter correct username")
            
        if len(data["email"]) < 6 or len(data["username"]) > 50:
            raise serializers.ValidationError("Enter correct email")
            
        return data
