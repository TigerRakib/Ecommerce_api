from rest_framework import serializers
from dataclasses import field
from .models import Product

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= "__all__"
        