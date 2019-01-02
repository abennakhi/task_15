from rest_framework import serializers
from .models import Restaurant

class RestaurantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','owner','name','description','opening_time','closing_time',]