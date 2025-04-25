from models.ticket_model import TicketModel
from models.ticket_search_criteria import TicketSearchCriteria


class ITicketService:
    def getAllTicket(criteria:TicketSearchCriteria) -> list[TicketModel]:
        pass

    def getOneTicket(id:int) -> TicketModel:
        pass

    def addTicket(TicketModel) -> int:
        pass

    def updateTicket(TicketModel) -> TicketModel:
        pass