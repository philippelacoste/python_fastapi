
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
    def getOneDevice(self,id:str) -> DeviceModel:
          #recupération des données de tests depuis le fichier json
        tickets:list = load_data()
        device_model= None

        for ticket in tickets:
            if  ticket["computer"]["id"] == id:
                device_model = ticket["computer"]
                return device_model
        #raise exception typée
        #soit je renvoie un champ nul et je laisse gérer l'appelant
        return device_model

    @override
    def addDevice(DeviceModel) -> str:
        pass

    @override
    def updateDevice(DeviceModel) -> DeviceModel:
        pass

    @override
    def removeDevice(id:str) -> str:
        pass


if __name__ == "__main__":
    service = DeviceServiceImpl()
    print("Hello", service.getOneDevice("pc006"))