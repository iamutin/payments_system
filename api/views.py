import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from payments.models import Organization
from api.serializers import OrganizationSerializer, PaymentSerializer
from payments.services import PaymentService


class WebhookView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        payment, created = PaymentService.create_payment(**serializer.validated_data)

        return Response(
            PaymentSerializer(payment).data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )


class BalanceView(APIView):
    def get(self, request, inn: str):
        try:
            organization = Organization.objects.get(inn=inn)
        except Organization.DoesNotExist:
            return Response(
                {"detail": "Organization not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(OrganizationSerializer(organization).data)
