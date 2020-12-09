from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    username   = serializers.CharField(max_length=100)
    email      = serializers.EmailField()
    first_name = serializers.CharField(max_length=50)
    last_name  = serializers.CharField(max_length=50)
