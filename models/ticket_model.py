from datetime import datetime

from pydantic import BaseModel

from models.device_model import DeviceModel
from models.enums import IMPACT, TICKET_STATUS
from models.user_model import UserModel


class TicketModel(BaseModel):
    id:int = -1
    title:str=""
    description:str=""
    creation_date:datetime = datetime.now()
    update_date:datetime = datetime.now()
    impact:IMPACT=IMPACT.MAJOR 
    status:TICKET_STATUS=TICKET_STATUS.OPEN
    # creator_user:UserModel=Nonev
    # computer:DeviceModel=None
    request_type:str=""