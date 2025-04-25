from datetime import datetime
from typing import Union
from fastapi import APIRouter
import urllib

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
        date_compare:datetime
        tickets:list=[]
        devices:list=[]
        filtered_devices:list=[]

        #parse q url parameters
        # date_update=2023-10-05T14:00:00Z&device_id=3 >>>>>>>>  {'date_update': ['2023-10-05T14:00:00Z'], 'device_id': ['3']}
        # params = urllib.parse.parse_qs(q)
        # date_compare_str = params["date_update"][0]
        # if date_compare_str:
        #     date_compare:datetime = datetime.fromisoformat(date_compare_str)

        #recupération des données de tests depuis le fichier json
        tickets:list = load_data()

        for ticket in tickets:
                device = ticket["computer"]
            # date_creation:datetime =  datetime.fromisoformat(device["creation_date"])
            # if date_compare.timestamp() > date_creation.timestamp():
                devices.append(device)
        filtered_devices = devices
        return filtered_devices


if __name__ == "__main__":
    myrouter = UserRouter()
    print("Hello", myrouter.get_one_device("pc006"))