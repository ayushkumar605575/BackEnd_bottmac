from rest_framework import serializers
from products.models import UserAccount

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'