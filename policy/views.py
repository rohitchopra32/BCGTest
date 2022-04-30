from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer
from django.db.models import Q
from policy.models import Policy, CustomerPolicies


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(OrderedDict([
             ('count', self.page.paginator.count),
             ('total_page', self.page.paginator.count // self.page_size),
             ('page_size', self.page_size),
             ('current', self.page.number),
             ('next', self.get_next_link()),
             ('previous', self.get_previous_link()),
             ('results', data)
         ]))


class PolicySerializer(ModelSerializer):
    class Meta:
        model = Policy
        fields = "__all__"


class PolicyView(ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    pagination_class = StandardResultsSetPagination


class CustomerPolicySerializer(ModelSerializer):
    class Meta:
        model = CustomerPolicies
        fields = "__all__"
        depth = 2


class CustomerPolicyView(ModelViewSet):
    queryset = CustomerPolicies.objects.all()
    serializer_class = CustomerPolicySerializer
    pagination_class = StandardResultsSetPagination


class SearchPolicy(APIView, StandardResultsSetPagination):
    model = CustomerPolicies
    serializer = CustomerPolicySerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        try:
            query = request.GET.get("query")

            qs = self.model.objects.filter(Q(policy_id=query) | Q(customer_id=query))
            qs = self.paginate_queryset(qs, request, view=self)
            data = self.serializer(qs, many=True).data
            return self.get_paginated_response(data)
        except Exception as error:
            return Response()