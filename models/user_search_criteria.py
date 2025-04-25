from datetime import datetime
from models.enums import IMPACT, TICKET_STATUS


class UserSearchCriteria:

    id:str = ""
    name:str=""
    email:str=""
    active:bool = False