from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from .views import BeerViewSet

router = DefaultRouter()
router.register(r'beers', BeerViewSet, basename='beer')

urlpatterns = router.urls
