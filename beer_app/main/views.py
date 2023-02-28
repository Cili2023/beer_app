from rest_framework.viewsets import ModelViewSet

from .models import Beer, Manufacturer, BeerType, Review
from .serializers import BeerSerializer, ManufacturerSerializer, BeerTypeSerializer, ReviewSerializer


class ManufacturerViewSet(ModelViewSet):

    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class BeerTypeViewSet(ModelViewSet):

    serializer_class = BeerTypeSerializer
    queryset = BeerType.objects.all()


class BeerViewSet(ModelViewSet):
    """ Beer ViewSet """

    serializer_class = BeerSerializer
    queryset = Beer.objects.all()



