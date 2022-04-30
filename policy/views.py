from collections import OrderedDict

from django.db.models import Q, Count
from django.db.models.functions import ExtractMonth, ExtractYear
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from policy.models import Policy, CustomerPolicies
from policy.serializers import PolicySerializer, CustomerPolicySerializer


class StandardResultsSetPagination(PageNumberPagination):
    """
    Custom paginator class to provide pagination functionality.
    """
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


class PolicyView(ModelViewSet):
    """
    API is used to perform operation on Policy Model.
    url => /api/policy/
    Allowed methods: GET, POST, PUT, PATCH, DELETE
    """
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer
    pagination_class = StandardResultsSetPagination


class CustomerPolicyView(ModelViewSet):
    """
    API is used to perform operation on CustomerPolicy Model.
    url => /api/policy/customer_policies/?region=<region>
    Allowed methods: GET, POST, PUT, PATCH, DELETE
    :param: query (Optional) it is used to filter result by customer_id and policy_id
    """
    queryset = CustomerPolicies.objects.all()
    serializer_class = CustomerPolicySerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        query = self.request.GET.get("query")
        if query:
            return self.queryset.filter(Q(policy_id=query) | Q(customer_id=query)).select_related("policy", "customer")
        return self.queryset


class GetPolicyByMonth(APIView):
    """
    API is used to get policies count per month of year
    url => /api/policy/get_policy_by_month/?region=<region>
    :param: region (Optional)
    accepted values = East, West, North, South

    response: [
    {
        "label": "1/2018",
        "value": "1"
    },
    {
        "label": "7/2018",
        "value": "72"
    }]

    """
    model = CustomerPolicies

    def get(self, request):
        try:
            region = request.GET.get("region")
            if region:
                queryset = self.model.objects.select_related("customer").filter(customer__region__iexact=region)
            else:
                queryset = self.model.objects.filter()

            queryset = queryset.annotate(
                month=ExtractMonth('date_of_purchase'),
                year=ExtractYear('date_of_purchase'), ) \
                .order_by() \
                .values('month', 'year') \
                .annotate(total=Count('*')) \
                .values('month', 'year', 'total')
            result = []
            for i in queryset:
                result.append({
                    "label": f"{i['month']}/{i['year']}",
                    "value": f"{i['total']}"
                })

            return Response(result, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({
                "error": str(error),
                "message": "Error Occurred while fetching data"
            }, status=status.HTTP_400_BAD_REQUEST)
