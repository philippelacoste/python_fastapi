from typing import Union
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from models.device_model import DeviceModel
from models.exceptions import TicketAppException
from services.impl.device_service_impl import DeviceServiceImpl
from services.ticket_service import IDeviceService
from fastapi_restful.cbv import cbv

device_service:IDeviceService = DeviceServiceImpl()

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
    
        device:DeviceModel = None
        device = device_service.getOneDevice(device_id)

        return device


    @router.get("/device")
    def get_all_device(self,q: Union[str, None] = None):
        
        filtered_devices:list=[]
        
        try:
            filtered_devices = device_service.getAllDevice()
        except TicketAppException as tick_app_ex:
            #erreur gérée dans mes services, déjà détaillée
            return JSONResponse(status_code=400)
        except Exception as ex:
            #erreurs non gérées à détailler
            return JSONResponse(status_code=500)

        return filtered_devices


if __name__ == "__main__":
    myrouter = UserRouter()
    print("Hello", myrouter.get_one_device("pc006"))