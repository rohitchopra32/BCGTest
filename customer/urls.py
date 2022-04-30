from rest_framework.routers import DefaultRouter

from customer.views import CustomerView

router = DefaultRouter()
router.register("", CustomerView, basename="customer")
