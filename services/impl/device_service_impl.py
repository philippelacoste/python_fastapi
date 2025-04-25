
from typing_extensions import override
from models.device_model import DeviceModel
from services.ticket_service import IDeviceService
from services.utils.data_services import load_data


class DeviceServiceImpl(IDeviceService):
    
    @override
    def getAllDevice(self) -> list[DeviceModel]:
        tickets:list=[]
        devices:list[DeviceModel]=[]

        #recupération des données de tests depuis le fichier json
        tickets:list = load_data()
        for ticket in tickets:
                device:DeviceModel = ticket["computer"]
                devices.append(device)

        return devices

    @override
    def getOneDevice(id:str) -> DeviceModel:
        #ICI le code qui récupère les données d'un device
        pass

    @override
    def addDevice(DeviceModel) -> str:
        pass

    @override
    def updateDevice(DeviceModel) -> DeviceModel:
        pass

    @override
    def removeDevice(id:str) -> str:
        pass