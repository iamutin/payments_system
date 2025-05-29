import logging

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from payments.models import Organization, Payment
from api.serializers import OrganizationSerializer, PaymentSerializer

logger = logging.getLogger(__name__)


class WebhookView(APIView):
    def post(self, request):
        data = request.data
        operation_id = data.get("operation_id")
        amount = data.get("amount")
        payer_inn = data.get("payer_inn")
        document_number = data.get("document_number")
        document_date = data.get("document_date")

        if Payment.objects.filter(operation_id=operation_id).exists():
            return Response(status=status.HTTP_200_OK)

        payment = Payment.objects.create(
            operation_id=operation_id,
            amount=amount,
            payer_inn=payer_inn,
            document_number=document_number,
            document_date=document_date,
        )

        organization, created = Organization.objects.get_or_create(inn=payer_inn)
        organization.balance += amount
        organization.save()

        logger.info(f"Balance updated for {payer_inn}: {organization.balance}")

        return Response(PaymentSerializer(payment).data, status=status.HTTP_201_CREATED)


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
