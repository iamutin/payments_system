from django.core.validators import RegexValidator
from django.db import models


class Organization(models.Model):
    inn = models.CharField(
        primary_key=True,
        max_length=12,
        validators=[
            RegexValidator(
                r"^(\d{10}|\d{12})$",
                message="ИНН должен содержать 10 или 12 цифр.",
            )
        ],
    )
    balance = models.IntegerField(default=0)

    def update_balance(self, amount: int) -> int:
        self.balance = models.F("balance") + amount
        self.save(update_fields=["balance"])
        self.refresh_from_db()
        return self.balance

    def __str__(self):
        return f"Organization {self.inn}"


class Payment(models.Model):
    operation_id = models.UUIDField(primary_key=True)
    amount = models.PositiveIntegerField()
    payer_inn = models.CharField(max_length=12)
    document_number = models.CharField(max_length=50)
    document_date = models.DateTimeField()

    def __str__(self):
        return f"Payment {self.operation_id} for {self.payer_inn}"
