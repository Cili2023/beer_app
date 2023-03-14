from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .mixins import FilterListMixin
from .models import Manufacturer, BeerType, Beer, Review
from .serializers import ManufacturerSerializer, BeerTypeSerializer, BeerSerializer, ReviewSerializer


class ManufacturerViewSet(FilterListMixin, ModelViewSet):

    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter
    )

    def list(self, request):
        try:
            serializer = self.get_serializer(
                self.filter_queryset(self.get_ordered_queryset(self.get_queryset(), 'name')), many=True
            )
            return Response(serializer.data)
        except Exception as e:
            return Response({'message': e}, status=status.HTTP_400_BAD_REQUEST)


class BeerTypeViewSet(FilterListMixin, ModelViewSet):
    serializer_class = BeerTypeSerializer
    queryset = BeerType.objects.all()

    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter
    )

    def list(self, request):
        try:
            serializer = self.get_serializer(
                self.filter_queryset(self.get_ordered_queryset(self.get_queryset(), 'name')), many=True
            )
            return Response(serializer.data)
        except Exception as e:
            return Response({'message': e}, status=status.HTTP_400_BAD_REQUEST)


class BeerViewSet(FilterListMixin, ModelViewSet):
    serializer_class = BeerSerializer
    queryset = Beer.objects.all()

    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter
    )

    search_fields = {
        'name'
    }

    def list(self, request):
        try:
            serializer = self.get_serializer(
                self.filter_queryset(self.get_ordered_queryset(self.get_queryset(), 'name')), many=True
            )
            print(serializer.data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'message': e}, status=status.HTTP_400_BAD_REQUEST)


class ReviewViewSet(FilterListMixin, ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter
    )

    def list(self, request):
        try:
            serializer = self.get_serializer(
                self.filter_queryset(self.get_ordered_queryset(self.get_queryset(), 'beer')), many=True
            )
            return Response(serializer.data)
        except Exception as e:
            return Response({'message': e}, status=status.HTTP_400_BAD_REQUEST)
