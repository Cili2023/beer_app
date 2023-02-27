from rest_framework.viewsets import ModelViewSet

from .models import Beer, Manufacturer
from .serializers import BeerSerializer, ManufacturerSerializer


class BeerViewSet(ModelViewSet):
    """ Beer ViewSet """

    serializer_class = BeerSerializer
    queryset = Beer.objects.all()


class ManufacturerViewSet(ModelViewSet):

    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
