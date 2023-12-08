from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import VendorViewSet, PurchaseOrderViewSet, HistoricalPerformanceViewSet

# Create a router and register the viewsets with it.
router = DefaultRouter()
router.register('vendors', VendorViewSet)
router.register('purchase_orders', PurchaseOrderViewSet)
router.register('historical_performances', HistoricalPerformanceViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token authentication view
    path('', include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
]
