from datetime import datetime

from models.enums import IMPACT


class DeviceModel:
    id:str = ""
    title:str = ""
    description:str = ""
    creation_date:datetime
    impact:IMPACT = IMPACT.BLOCKING