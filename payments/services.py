import logging

from django.db import transaction
from .models import Organization, Payment
from datetime import datetime
from uuid import UUID

logger = logging.getLogger(__name__)


class PaymentService:
    @staticmethod
    @transaction.atomic
    def create_payment(
        operation_id: UUID,
        amount: int,
        payer_inn: str,
        document_number: str,
        document_date: datetime,
    ) -> tuple[Payment, bool]:
        """
        Создает платеж, если он не существует.
        Возвращает кортеж: (payment, created)
        """
        payment, created = Payment.objects.get_or_create(
            operation_id=operation_id,
            defaults={
                "amount": amount,
                "payer_inn": payer_inn,
                "document_number": document_number,
                "document_date": document_date,
            },
        )

        if created:
            organization, _ = Organization.objects.get_or_create(inn=payer_inn)
            balance = organization.update_balance(amount=amount)
            logger.info(f"Обновился баланс организации {payment.payer_inn}: {balance}")

        return payment, created
