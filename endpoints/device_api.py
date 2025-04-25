from datetime import datetime
from typing import Union
from fastapi import APIRouter
import urllib

from services.impl.device_service_impl import DeviceServiceImpl
from services.ticket_service import IDeviceService
from services.utils.data_services import load_data
from fastapi_restful.cbv import cbv



router = APIRouter()

@cbv(router)
class UserRouter:

    @router.post("/device")
    def add_device(self,device):
        print("add_device")

    @router.put("/device")
    def update_device(self,device):
        print("update_device")

    @router.get("/device/{device_id}")
    def get_one_device(self,device_id: str):
    
        devices:list=[]
        #recupération des données de tests depuis le fichier json
        tickets:list = load_data()

        for ticket in tickets:
            if  ticket["computer"]["id"] == device_id:
                devices.append(ticket["computer"])

        return devices

    @router.get("/device")
    def get_all_device(self,q: Union[str, None] = None):
        
        filtered_devices:list=[]
        device_service:IDeviceService = DeviceServiceImpl()
        filtered_devices = device_service.getAllDevice()
    
        return filtered_devices


if __name__ == "__main__":
    myrouter = UserRouter()
    print("Hello", myrouter.get_one_device("pc006"))