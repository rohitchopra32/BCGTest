from django.urls import path
from rest_framework.routers import DefaultRouter

from policy.views import PolicyView, CustomerPolicyView


router = DefaultRouter()
router.register("customer_policies", CustomerPolicyView, basename="customer_policies")
router.register("", PolicyView, basename="policy")
