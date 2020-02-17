from appdirs import unicode

from .models.ParsedOperation import ParsedOperation, OperationType


def parse_operation(operation, acccount):
    amount_get_text = operation.amount.get_text()
    parsed = ParsedOperation(account=acccount, amount=float(unicode(amount_get_text)),
                             description=operation.description.get_text(), orderDate="Today", execDate="Today")
    parsed.Type = OperationType.INCOMING if parsed.amount > 0 else OperationType.OUTGOING
    return parsed
