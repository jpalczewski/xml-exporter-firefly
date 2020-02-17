from .models.Operation import Operation, OperationType


class Parser:
    def __init__(self, account):
        """
        :param account: src/dest of transaction, despite of the type.
        """
        self.account = account

    def parse_operation(self, operation):
        try:
            parsed = Operation(
                account=self.account,
                amount=float(operation.amount.get_text()),
                description=operation.description.get_text(),
                orderDate=operation.find("order-date").get_text(),
                execDate=operation.find("exec-date").get_text(),
                currencyCode=operation.amount.attrs["curr"]
            )
            parsed.Type = (
                OperationType.INCOMING if parsed.amount > 0 else OperationType.OUTGOING
            )
        except AttributeError as e:
            raise ValueError(e, f"Malformed operation")
        return parsed
