from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Beer
from .serializers import BeerSerializer


class BeerViewSet(ModelViewSet):
    """ Beer ViewSet """

    serializer_class = BeerSerializer
    queryset = Beer.objects.all()

    # def list(self, request):
    #     queryset = Beer.objects.all()
    #     serializer = BeerSerializer(queryset, many=True)
    #     return Response(serializer.data)
