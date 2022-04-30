from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from customer.models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class CustomerView(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class LoadData(APIView):
    def post(self, request):
        """{
            "Policy_id": "policy_id",
            "Date of Purchase": "1/16/2018",
            "Customer_id": 400,
            "Fuel": "CNG",
            "VEHICLE_SEGMENT": "A",
            "Premium": 958,
            "bodily injury liability": 0,
            "personal injury protection": 0,
            "property damage liability": 0,
            "collision": 1,
            "comprehensive": 1,
            "Customer_Gender": "Male",
            "Customer_Income group": "0- $25K",
            "Customer_Region": "North",
            "Customer_Marital_status": 0
        },"""
        data = request.data
        from policy.models import Policy, CustomerPolicies
        from datetime import datetime
        for i in data:
            policy = Policy.objects.get(id=i["Policy_id"])
            customer = Customer.objects.get(id=i["Customer_id"])
            d = datetime.strptime(i["Date of Purchase"], "%m/%d/%Y")
            obj, created = CustomerPolicies.objects.get_or_create(
                policy=policy,
                customer=customer,
                defaults={
                    "date_of_purchase": d
                }
            )
            print(obj, created)
