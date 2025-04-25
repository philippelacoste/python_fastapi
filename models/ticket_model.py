from datetime import datetime

from models.device_model import DeviceModel
from models.enums import IMPACT, TICKET_STATUS
from models.user_model import UserModel


class TicketModel:
    id:int = -1
    title:str=""
    description:str=""
    creation_date:datetime = datetime.now()
    update_date:datetime
    impact:IMPACT=IMPACT.MAJOR 
    status:TICKET_STATUS=TICKET_STATUS.OPEN
    creator_user:UserModel=None
    computer:DeviceModel=None
    request_type:str=""