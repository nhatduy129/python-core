from rest_framework import serializers
from .models import Category
from .models import Partnership


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = '__all__'
