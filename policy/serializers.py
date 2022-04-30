from rest_framework.serializers import ModelSerializer

from policy.models import Policy, CustomerPolicies


class PolicySerializer(ModelSerializer):
    class Meta:
        model = Policy
        fields = "__all__"


class CustomerPolicySerializer(ModelSerializer):
    class Meta:
        model = CustomerPolicies
        fields = "__all__"
        depth = 2