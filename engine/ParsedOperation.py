from dataclasses import dataclass, field
from enum import Enum


class OperationType(Enum):
    INCOMING = 1
    OUTGOING = 2
    UNKNOWN = 3


@dataclass
class ParsedOperation:
    execDate: str
    orderDate: str
    description: str
    amount: float
    account: str
    Type: OperationType = field(default=OperationType.UNKNOWN, init=False)

