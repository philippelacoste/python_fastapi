from datetime import datetime
from log.decorators import log_method
from models.enums import TICKET_STATUS
from models.ticket_model import TicketModel
from models.ticket_search_criteria import TicketSearchCriteria
from services.ticket_service import ITicketService
from typing_extensions import override

from services.utils.data_services import load_data

class TicketServiceImpl(ITicketService):

    @log_method
    @override
    def getAllTicket(self,criteria:TicketSearchCriteria=None) -> list[TicketModel]:
        filtered_tickets:list[TicketModel] = []
         #recupération des données de tests depuis le fichier json
        tickets:list = load_data()
        
        for ticket in tickets:
            date_creation:datetime =  datetime.fromisoformat(ticket["creation_date"])
            ticket_model:TicketModel = TicketModel()
            #adapt data to model
            ticket_model.status = TICKET_STATUS.IN_PROGRESS

            if not criteria :
                filtered_tickets.append(ticket_model.__dict__)
                
            if criteria and criteria.creation_date and (criteria.creation_date.timestamp() > date_creation.timestamp()):
                filtered_tickets.append(ticket_model)
        
        return filtered_tickets
    
    @log_method
    @override
    def getOneTicket(self,id:int) -> TicketModel:
        ticket_model:TicketModel = None
        tickets:list = load_data()

        for ticket in tickets:
            if  ticket["id"] == id.__str__():
                ticket_model = ticket
                return ticket_model
        #TODO:raise exception
        return ticket_model
    
    @override
    def addTicket(self,TicketModel) -> int:
        pass

    @override
    def updateTicket(self,TicketModel) -> TicketModel:
        pass
 
if __name__ == "__main__":
    service = TicketServiceImpl()

    print("Hello", service.getAllTicket())