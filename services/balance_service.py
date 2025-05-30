from payments.models import Organization


class BalanceService:
    @staticmethod
    def get_organization_balance(inn: str) -> Organization:
        """
        Получение текущего баланса организации по её ИНН.
        :param inn: ИНН организации
        :return: объект Organization или raise DoesNotExist
        """
        return Organization.objects.get(inn=inn)
