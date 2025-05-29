from django.db import models


class Organization(models.Model):
    inn = models.CharField(primary_key=True, max_length=12)
    balance = models.IntegerField(default=0)

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
