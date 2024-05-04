from rest_framework.routers import DefaultRouter
from client.api.views import ClintViewSet

router = DefaultRouter()
router.register('clients', ClintViewSet, basename='client')
urlpatterns = router.urls
