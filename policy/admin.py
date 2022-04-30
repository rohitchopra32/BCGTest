from django.contrib import admin

from policy.models import Policy, CustomerPolicies

admin.site.register(Policy)
admin.site.register(CustomerPolicies)
