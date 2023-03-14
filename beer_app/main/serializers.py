from .models import Manufacturer, BeerType, Beer, Review
from rest_framework import serializers


class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ['name', 'address', 'town', 'postal_code']


class BeerTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BeerType
        fields = ['name', 'description']


class BeerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beer
        fields = [
            'beer_type',
            'manufacturer',
            'name',
            'alcohol_percentage',
            'color',
            'aroma_choice',
            'water_percentage',
            'barley_percentage',
            'hop_percentage',
            'yeast_percentage',
            'current_rating'
        ]


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['grade', 'beer', 'description', 'created_at']

