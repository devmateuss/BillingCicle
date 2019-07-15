from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from BillingCicle.models import BillingCicle, Credit, Debit
from BillingCicle.serializers import BillingCicleSerializer


class BillingCicleViewSet(viewsets.ModelViewSet):
    queryset = BillingCicle.objects.all()
    serializer_class = BillingCicleSerializer

    @action(methods=['GET'], detail=False)
    def count(self, request):
        value = BillingCicle.objects.count()

        return Response({'value': value})

    @action(methods=['GET'], detail=False)
    def summary(self, request):
        credit = Credit.objects.all().aggregate(Sum('value'))
        debit = Debit.objects.all().aggregate(Sum('value'))

        return Response({'credit': credit['value__sum'], 'debit': debit['value__sum']})
