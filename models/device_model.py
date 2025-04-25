from datetime import datetime

from models.enums import DEVICE_STATUS


class DeviceModel:
    id:str = ""
    title:str = ""
    description:str = ""
    creation_date:datetime
    status:DEVICE_STATUS = DEVICE_STATUS.IN_USE