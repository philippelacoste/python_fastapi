
from datetime import datetime
from typing import Union
from fastapi import APIRouter
import urllib

from fastapi.responses import JSONResponse

from services.utils.data_services import DataFileLoadException, load_data
from fastapi_restful.cbv import cbv



router = APIRouter()


class TicketApplicationException(Exception):
    pass

@cbv(router)
class TicketRouter:

    @router.post("/ticket")
    def add_ticket(self,ticket):
        print("add_ticket")

    @router.put("/ticket")
    def update_ticket(self,ticket):
        print("update_ticket")

    @router.get("/ticket/{ticket_id}")
    def get_one_ticket(self,ticket_id: int):
    
        filtered_tickets:list=[]
        #recupération des données de tests depuis le fichier json
        
        try:
            tickets:list = load_data()
        except DataFileLoadException as data_exc:
            response = JSONResponse(status_code=400,
                         content={
                            "message":"Erreur lors du chargement des données"
                         }
                         )
            print("Erreur lors du chargement des données")
        except Exception as exc:
            response = JSONResponse(status_code=400,
                         content={
                            "message":"Erreur lors du chargement des données, exception non gérée"
                         }
                         )
            print("exception non gérée lors du chargement des données")
            return response

        for ticket in tickets:
            if  ticket["id"] == ticket_id.__str__():
                filtered_tickets.append(ticket)

        if filtered_tickets.__len__() == 0:
            # raise TicketApplicationException("Erreur pas de tickets")
            response = JSONResponse(status_code=404,
                         content={
                            "message":"Pas de ticket !"
                         }
                         )
            print("Pas de ticket")
            return response


        return filtered_tickets

    @router.get("/ticket")
    def get_all_ticket(self,q: Union[str, None] = None):
        date_compare:datetime
        filtered_tickets:list=[]

        #parse q url parameters
        # date_update=2023-10-05T14:00:00Z&user_id=3 >>>>>>>>  {'date_update': ['2023-10-05T14:00:00Z'], 'user_id': ['3']}
        params = urllib.parse.parse_qs(q)
        date_compare_str = params["date_update"][0]
        if date_compare_str:
            date_compare:datetime = datetime.fromisoformat(date_compare_str)

        #recupération des données de tests depuis le fichier json
        tickets:list = load_data()

        for ticket in tickets:
            date_creation:datetime =  datetime.fromisoformat(ticket["creation_date"])
            if date_compare.timestamp() > date_creation.timestamp():
                filtered_tickets.append(ticket)

        return filtered_tickets

        
        # 1 identifier uniquement les dates inférieur à la date entrée
        # 2 mettre la date comme paramètre à la méthode de service

        # 3 extraire dans une méthode (def) le chargement des tickets
        # 4 retourner la liste filtrée
        # 5 gérer le paramètre q 
        
        # 6 renommer la méthode en getAllTicket
        # 7 créer une méthode getOneTicket(id:int)


if __name__ == "__main__":
    myrouter = TicketRouter()
    print("Hello", myrouter.get_one_ticket(33))