from django.urls import path
from rest_framework.routers import DefaultRouter

from policy.views import PolicyView, CustomerPolicyView, GetPolicyByMonth

router = DefaultRouter()
router.register("customer_policies", CustomerPolicyView, basename="customer_policies")
router.register("", PolicyView, basename="policy")

urlpatterns = [
    path("get_policy_by_month/", GetPolicyByMonth.as_view(), name="get_policy_by_month"),
]

urlpatterns.extend(router.urls)
