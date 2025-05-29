from rest_framework import serializers

from payments.models import Payment, Organization


class PaymentSerializer(serializers.ModelSerializer):
    operation_id = serializers.UUIDField(validators=[])

    class Meta:
        model = Payment
        fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"
