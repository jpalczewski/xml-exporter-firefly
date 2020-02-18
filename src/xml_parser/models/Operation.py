from dataclasses import dataclass, field
from enum import Enum, auto


class OperationDirection(Enum):
    INCOMING = 1
    OUTGOING = 2
    UNKNOWN = 3


class OperationType(Enum):
    BLIK = auto()
    CARD_PAYMENT = auto()
    PAYMENT = auto()


operationTypeDict = {
    "Obciążenie": OperationType.PAYMENT
}


@dataclass
class Operation:
    execDate: str
    orderDate: str
    description: str
    amount: float
    account: str
    currencyCode: str
    type: str
    direction: OperationDirection = field(default=OperationDirection.UNKNOWN, init=False)
