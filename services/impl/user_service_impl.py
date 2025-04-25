
from typing_extensions import override
from log.decorators import log_method
from models.device_model import DeviceModel
from models.exceptions import NoDataException
from models.user_model import UserModel
from models.user_search_criteria import UserSearchCriteria
from services.ticket_service import  IUserService
from services.utils.data_services import load_data


class UserServiceImpl(IUserService):
    
    @log_method
    @override
    def getAllUser(self, criteria:UserSearchCriteria) -> list[UserModel]:
        users:list[UserModel] = []
        tickets:list = load_data()

        for ticket in tickets:
            users.append(ticket["creator_user"])
            
        if criteria and criteria.name != "":
            filtered_users = filter(lambda user: user["name"] == criteria.name ,users)
            return list(filtered_users)

        return users
    
    @override
    def getOneUser(self,id:str) -> UserModel:
        user:UserModel = None

        #recupération des données de tests depuis le fichier json
        tickets:list = load_data()

        for ticket in tickets:
            if  ticket["creator_user"]["id"] == id:
                user = ticket["creator_user"]
                return user
        
        raise NoDataException()


    def addUser(UserModel) -> str:
        pass

    def updateUser(UserModel) -> UserModel:
        pass

    def removeUser(id:str) -> str:
        pass

if __name__ == "__main__":
    service = UserServiceImpl()
    print("Hello", service.getAllUser())