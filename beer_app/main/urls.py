from rest_framework.routers import DefaultRouter

from .views import BeerViewSet, ManufacturerViewSet

router = DefaultRouter()
router.register(r'beers', BeerViewSet, basename='beer')
router.register(r'manufacturers', ManufacturerViewSet, basename='manufacturer')

urlpatterns = router.urls
