
from datetime import datetime
from typing import Union
from fastapi import APIRouter
import urllib

from fastapi.responses import JSONResponse

from models.ticket_model import TicketModel
from models.ticket_search_criteria import TicketSearchCriteria
from services.impl.ticket_service_impl import TicketServiceImpl
from services.ticket_service import ITicketService
from services.utils.data_services import DataFileLoadException, load_data
from fastapi_restful.cbv import cbv



router = APIRouter()

ticket_service:ITicketService = TicketServiceImpl()

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
    
        ticket:TicketModel=None
              
        ticket = ticket_service.getOneTicket(ticket_id)


        return ticket

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
        
        #add criteria
        criteria:TicketSearchCriteria = TicketSearchCriteria()
        criteria.creation_date = date_compare

        filtered_tickets = ticket_service.getAllTicket(criteria)

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