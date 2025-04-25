
from datetime import datetime
from typing import Union
from fastapi import APIRouter
import urllib

from services.utils.data_services import load_data
from fastapi_restful.cbv import cbv



router = APIRouter()

@cbv(router)
class UserRouter:

    @router.post("/user")
    def add_user(self,user):
        print("add_user")

    @router.put("/user")
    def update_user(self,user):
        print("update_user")

    @router.get("/user/{user_id}")
    def get_one_user(self,user_id: str):
    
        filtered_users:list=[]
        #recupération des données de tests depuis le fichier json
        tickets:list = load_data()

        for ticket in tickets:
            if  ticket["creator_user"]["id"] == user_id:
                filtered_users.append(ticket["creator_user"])

        return filtered_users

    @router.get("/user")
    def get_all_user(self,q: Union[str, None] = None):
        date_compare:datetime
        users:list=[]
        filtered_users:list=[]

        #parse q url parameters
        # date_update=2023-10-05T14:00:00Z&user_id=3 >>>>>>>>  {'date_update': ['2023-10-05T14:00:00Z'], 'user_id': ['3']}
        # params = urllib.parse.parse_qs(q)
        # date_compare_str = params["date_update"][0]
        # if date_compare_str:
        #     date_compare:datetime = datetime.fromisoformat(date_compare_str)

        #recupération des données de tests depuis le fichier json
        tickets:list = load_data()

        for ticket in tickets:
            # date_creation:datetime =  datetime.fromisoformat(ticket["creation_date"])
            # if date_compare.timestamp() > date_creation.timestamp():
            users.append(ticket["creator_user"])
 
        filtered_users = users

        return filtered_users


if __name__ == "__main__":
    myrouter = UserRouter()
    print("Hello", myrouter.get_one_user("u011").__len__())