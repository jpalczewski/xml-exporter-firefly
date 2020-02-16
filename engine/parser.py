from pprint import pprint

from appdirs import unicode
from firefly_iii_client.models import transaction_split

from engine.ParsedOperation import ParsedOperation, OperationType


def parse_operation(operation, acccount):
    amount_get_text = operation.amount.get_text()
    parsed = ParsedOperation(account=acccount, amount=float(unicode(amount_get_text)), description=operation.description.get_text(), orderDate="Today", execDate="Today")
    parsed.Type = OperationType.INCOMING if parsed.amount > 0 else OperationType.OUTGOING
    pprint(parsed)
    return parsed
