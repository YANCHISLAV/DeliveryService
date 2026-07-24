from enum import Enum

class OrderStatus(Enum):
    CREATED = 'CREATED',
    FAILED = 'FAILED',
    COMPLETED = 'COMPLETED'
