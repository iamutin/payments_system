import logging

from django.db import transaction
from datetime import datetime
from uuid import UUID

from payments.models import Organization, Payment

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
        Создание нового платежа или получение существующего, с защитой от дубликатов и обновлением баланса организации.

        :param operation_id: идентификатор операции (UUID)
        :param amount: сумма платежа (целое число)
        :param payer_inn: ИНН плательщика (строка)
        :param document_number: номер документа (строка)
        :param document_date: дата документа (datetime)
        :return: кортеж (Payment, bool), где Payment — созданный платеж, bool — признак того, был ли платеж создан
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
