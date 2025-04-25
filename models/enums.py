from enum import Enum


class DEVICE_STATUS(str,Enum):
    IN_USE = "InUse"
    MAINTENANCE = "Maintenance"
    ORDER_INP_ROGRESS = "OrderInProgress"

class TICKET_STATUS(str,Enum):
    OPEN = "Open"
    IN_PROGRESS = "InProgress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"
    CANCELLED = "Cancelled"

class IMPACT(str,Enum):
    BLOCKING = "Blocking"
    MAJOR = "Major"
    MINOR = "Minor"