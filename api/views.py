from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from payments.models import Organization
from api.serializers import OrganizationSerializer, PaymentSerializer
from services.balance_service import BalanceService
from services.payment_service import PaymentService


class WebhookView(APIView):
    def post(self, request: Request) -> Response:
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        payment, created = PaymentService.create_payment(**serializer.validated_data)

        return Response(
            PaymentSerializer(payment).data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )


class BalanceView(APIView):
    def get(self, request: Request, inn: str) -> Response:
        try:
            organization = BalanceService.get_organization_balance(inn)
            return Response(OrganizationSerializer(organization).data)
        except Organization.DoesNotExist:
            return Response(
                {"detail": "Организация не найдена."},
                status=status.HTTP_404_NOT_FOUND,
            )
