from rest_framework import serializers
from .models import Good, Token


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('token')

class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ('name', 'amount', 'price')