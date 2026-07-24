
from enum import Enum
class TransactionStatus(Enum):
    COMPLETED = 'COMPLETED',
    FAILED = "FAILED",
    PENDING = "PENDING"