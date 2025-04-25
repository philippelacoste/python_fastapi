from datetime import datetime

from models.enums import DEVICE_STATUS


class DeviceModel:
    id:str = ""
    configuration:str = ""
    status:DEVICE_STATUS = DEVICE_STATUS.IN_USE