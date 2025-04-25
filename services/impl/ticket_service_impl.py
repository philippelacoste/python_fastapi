from datetime import datetime
import json
from log.decorators import log_method
from models.enums import IMPACT, TICKET_STATUS
from models.ticket_model import TicketModel
from models.ticket_search_criteria import TicketSearchCriteria
from services.ticket_service import ITicketService
from typing_extensions import override

from services.utils.data_services import load_data

class TicketServiceImpl(ITicketService):

    def to_obj(self, in_dict:dict, ticket_model:TicketModel):
            """ Method to convert a dict to an object (only first lvl attribute)"""
            for key, val in in_dict.items():
                 setattr(ticket_model,key,val)

    @log_method
    @override
    def getAllTicket(self,criteria:TicketSearchCriteria=None) -> list[TicketModel]:
        filtered_tickets:list[TicketModel] = []
         #recupération des données de tests depuis le fichier json
        tickets:list = load_data()

        # ## cette lambda 
        # my_tickets = []
        # my_tickets = list(filter(lambda ticket: is_ticket_ok(ticket,criteria), tickets))

        # ### equivalent à 
        # my_tickets = []
        # for  ticket in tickets:
        #     if  ticket["impact"] == "Major":
        #         my_tickets.append(ticket)
        # print(list(my_tickets).__len__())
        # #####
        
        for ticket in tickets:
            date_creation:datetime =  datetime.fromisoformat(ticket["creation_date"])
            ticket_model:TicketModel = TicketModel()
            
            self.to_obj(ticket, ticket_model)
            #adapt data to model
            ticket_model.status = TICKET_STATUS(ticket_model.status)
            ticket_model.impact = IMPACT(ticket_model.impact)

            if not criteria :
                filtered_tickets.append(ticket_model)
                
            if criteria:
                is_filtered:bool = True
                #date_creation
                is_filtered = is_filtered and criteria.creation_date and (criteria.creation_date.timestamp() > date_creation.timestamp())

                #status
                is_filtered = is_filtered and criteria.status and (criteria.status == ticket_model.status)

                #impact
                is_filtered = is_filtered and criteria.impact and (criteria.impact == ticket_model.impact)

                if is_filtered:
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
    def addTicket(self,ticket:TicketModel) -> int:
        pass

    @override
    def updateTicket(self,ticket:TicketModel) -> TicketModel:
        pass
 
if __name__ == "__main__":
    service = TicketServiceImpl()

    print("Hello", service.getAllTicket())