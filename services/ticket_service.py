from models.device_model import DeviceModel
from models.ticket_model import TicketModel
from models.ticket_search_criteria import TicketSearchCriteria
from models.user_model import UserModel


class ITicketService:

    def getAllTicket(criteria:TicketSearchCriteria) -> list[TicketModel]:
        """Get all available tickets using criteria"""
        pass

    def getOneTicket(id:int) -> TicketModel:
        pass

    def addTicket(TicketModel) -> int:
        pass

    def updateTicket(TicketModel) -> TicketModel:
        pass


class IDeviceService:
    def getAllDevice() -> list[DeviceModel]:
        """Get all available devices"""
        pass

    def getOneDevice(id:str) -> DeviceModel:
        pass

    def addDevice(DeviceModel) -> str:
        pass

    def updateDevice(DeviceModel) -> DeviceModel:
        pass

    def removeDevice(id:str) -> str:
        pass


class IUserService:
    def getAllUser() -> list[UserModel]:
        pass

    def getOneUser(id:str) -> UserModel:
        pass

    def addUser(UserModel) -> str:
        pass

    def updateUser(UserModel) -> UserModel:
        pass

    def removeUser(id:str) -> str:
        pass