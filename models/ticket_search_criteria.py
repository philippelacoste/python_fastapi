from datetime import datetime
from models.enums import IMPACT, TICKET_STATUS


class TicketSearchCriteria:

    id:int = -1
    creation_date:datetime = datetime.now()
    update_date:datetime
    impact:IMPACT=IMPACT.MAJOR 
    status:TICKET_STATUS=TICKET_STATUS.OPEN
    user_id:str=""
    computer_id:str=""
    request_type:str=""