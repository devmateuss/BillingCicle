from rest_framework import serializers

from BillingCicle.models import BillingCicle, Credit, Debit



class CreditsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = '__all__'


class DebitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debit
        fields = '__all__'


class BillingCicleSerializer(serializers.ModelSerializer):
    credits = CreditsSerializer(many=True, read_only=True)
    debits = DebitsSerializer(many=True, read_only=True)

    class Meta:
        model = BillingCicle
        fields = ('id', 'name', 'month', 'year', 'credits', 'debits',)

    def create(self, request, *args, **kwargs):
        data = request

        billingCicle = BillingCicle.objects.create(
            name=data['name'],
            month=data['month'],
            year=data['year'],
        )

        for credit in data['credits']:
            billingCicle.credits.create(
                name=credit['name'],
                value=credit['value'])

        for debit in data['debits']:
            billingCicle.debits.create(
                name=debit['name'],
                value=debit['value'],
                status=debit['status'])

        return billingCicle