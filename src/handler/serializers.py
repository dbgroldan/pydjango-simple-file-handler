from rest_framework import serializers
from .models import File, Client

class FileSerializer(serializers.ModelSerializer):
        class Meta():
            model = File
            fields = '__all__' 

class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta():
        model = Client
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user