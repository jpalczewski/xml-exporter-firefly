from bs4 import BeautifulSoup

from .models.Operation import Operation, OperationDirection


class Parser:
    def __init__(self, account, savings_account=None):
        """
        :param savings_account: savings account related with main account
        :param account: src/dest of transaction, despite of the type.
        """
        self.account = account
        self.savings_account = savings_account

    def parse_operation(self, operation):
        try:
            if not isinstance(operation, BeautifulSoup):
                raise TypeError(f"Malformed argument")

            parsed = Operation(
                account=self.account,
                amount=float(operation.amount.get_text()),
                description=operation.description.get_text(),
                orderDate=operation.find("order-date").get_text(),
                execDate=operation.find("exec-date").get_text(),
                currencyCode=operation.amount.attrs["curr"],
                type=operation.find("type").get_text(),
            )
            parsed.direction = (
                OperationDirection.INCOMING
                if parsed.amount > 0
                else OperationDirection.OUTGOING
            )
        except AttributeError as e:
            raise ValueError(e, f"Malformed operation")
        return parsed
