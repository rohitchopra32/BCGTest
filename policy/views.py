from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer

from policy.models import Policy, CustomerPolicies


class PolicySerializer(ModelSerializer):
    class Meta:
        model = Policy
        fields = "__all__"


class PolicyView(ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer


class CustomerPolicySerializer(ModelSerializer):
    class Meta:
        model = CustomerPolicies
        fields = "__all__"
        depth = 2


class CustomerPolicyView(ModelViewSet):
    queryset = CustomerPolicies.objects.all()
    serializer_class = CustomerPolicySerializer
