
from typing import TypeVar


T = TypeVar("T")

class TicketAppException(Exception):
    error: T
    http_code:int = 500


class NotImplementedException(TicketAppException):
    http_code:int = 302


class NoDataException(TicketAppException):
    http_code:int = 404