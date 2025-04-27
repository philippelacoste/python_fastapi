
from datetime import datetime
import traceback
from typing import Union
from fastapi import APIRouter
import urllib

from fastapi.responses import JSONResponse
from pydantic import Field

from models.device_model import DeviceModel
from models.enums import IMPACT, TICKET_STATUS
from models.exceptions import NoDataException, TicketAppException
from models.ticket_model import TicketModel
from models.ticket_search_criteria import TicketSearchCriteria
from models.user_model import UserModel
from services.impl.ticket_service_impl import TicketServiceImpl
from services.ticket_service import ITicketService
from services.utils.data_services import DataFileLoadException, load_data
from fastapi_restful.cbv import cbv



router = APIRouter()

ticket_service:ITicketService = TicketServiceImpl()

class TicketApplicationException(Exception):
    pass

class TicketSchema(TicketModel):
    id:int = Field(-1)
    title:str=Field("")
    description:str=Field("")
    creation_date:datetime = Field(None)
    update_date:datetime = Field(None)
    impact:IMPACT = Field(IMPACT.MAJOR)
    status:TICKET_STATUS= Field(TICKET_STATUS.IN_PROGRESS)
    # creator_user:UserModel=Field(None)
    # computer:DeviceModel=Field(None)
    request_type:str=Field("")

@cbv(router)
class TicketRouter:

    @router.post("/ticket")
    def add_ticket(self,ticket):
       
        print("add_ticket")

    @router.put("/ticket")
    def update_ticket(self,ticket:TicketSchema):
        ticket_service.updateTicket(ticket)

    @router.get("/ticket/{ticket_id}")
    def get_one_ticket(self,ticket_id: int):
    
        ticket:TicketModel=None
              
        try:
            ticket = ticket_service.getOneTicket(ticket_id)

        except NoDataException as no_data_ex:
            return JSONResponse(status_code=no_data_ex.http_code,
                         content={
                             "message":f"No ticket found with this id > {ticket_id}"
                         })
        except TicketAppException as app_exc:
            return JSONResponse(status_code=app_exc.http_code,
                         content={
                             "message":f"Error during ticket search > {ticket_id}"
                         })
        except DataFileLoadException as df_exc:
            return JSONResponse(status_code=df_exc.http_code,
                         content={
                             "message":f"Error while loading data > {ticket_id}"
                         })
        except Exception as exc:
            return JSONResponse(status_code=500,
                         content={
                             "message":f"Unknown error > {traceback.format_exception_only(exc)}"
                         })
       
        # ou return ticket
        return JSONResponse(status_code=200,
                         content={
                             "ticket": ticket
                         })

    @router.get("/ticket")
    def get_all_ticket(self,q: Union[str, None] = None):
        date_compare:datetime
        filtered_tickets:list=[]
        criteria:TicketSearchCriteria = None
        #parse q url parameters
        # date_update=2023-10-05T14:00:00Z&status=Open >>>>>>>>  {'date_update': ['2023-10-05T14:00:00Z'], 'user_id': ['3']}
        params = urllib.parse.parse_qs(q)
        if params :
            #add criteria
            criteria = TicketSearchCriteria()
            if 'date_update' in params:
                date_compare_str = params["date_update"][0]
                if date_compare_str:
                    date_compare:datetime = datetime.fromisoformat(date_compare_str)
                    criteria.creation_date = date_compare

            if 'status' in params:
                status_compare:TICKET_STATUS = TICKET_STATUS(params["status"][0])
                criteria.status = status_compare

            if 'impact' in params:
                impact_compare:IMPACT = IMPACT(params["impact"][0])
                criteria.impact = impact_compare

        filtered_tickets = ticket_service.getAllTicket(criteria)

        return filtered_tickets


if __name__ == "__main__":
    myrouter = TicketRouter()
    print("Hello", myrouter.get_one_ticket(33))