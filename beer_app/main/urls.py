from rest_framework.routers import DefaultRouter

from .views import BeerViewSet, ManufacturerViewSet, BeerTypeViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'beers', BeerViewSet, basename='beer')
router.register(r'manufacturers', ManufacturerViewSet, basename='manufacturer')
router.register(r'beer types', BeerTypeViewSet, basename='beer type')
router.register(r'reviews', ReviewViewSet, basename='review')
urlpatterns = router.urls
