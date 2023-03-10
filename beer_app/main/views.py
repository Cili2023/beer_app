from rest_framework.viewsets import ModelViewSet

from beer_app.main.mixin import FilterMixin
from .models import Manufacturer, BeerType, Beer, Review
from .serializers import ManufacturerSerializer, BeerTypeSerializer, BeerSerializer, ReviewSerializer


class ManufacturerViewSet(ModelViewSet, FilterMixin):

    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class BeerTypeViewSet(ModelViewSet, FilterMixin):
    serializer_class = BeerTypeSerializer
    queryset = BeerType.objects.all()


class BeerViewSet(ModelViewSet, FilterMixin):
    serializer_class = BeerSerializer
    queryset = Beer.objects.all()


class ReviewViewSet(ModelViewSet, FilterMixin):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
