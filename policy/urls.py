from django.urls import path
from rest_framework.routers import DefaultRouter

from policy.views import PolicyView, CustomerPolicyView, SearchPolicy


router = DefaultRouter()
router.register("customer_policies", CustomerPolicyView, basename="customer_policies")
router.register("", PolicyView, basename="policy")

urlpatterns = [
    path('search/', SearchPolicy.as_view(), name="search_policies")
]

urlpatterns.extend(router.urls)