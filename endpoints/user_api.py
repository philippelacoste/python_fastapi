
from datetime import datetime
import traceback
from typing import Union
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from models.exceptions import NoDataException, TicketAppException
from models.user_model import UserModel
from services.impl.user_service_impl import UserServiceImpl
from services.ticket_service import IUserService
from fastapi_restful.cbv import cbv

from services.utils.data_services import DataFileLoadException

user_service:IUserService = UserServiceImpl()

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
        user:UserModel = None

        try:
            user = user_service.getOneUser(user_id)

        except NoDataException as no_data_ex:
            return JSONResponse(status_code=no_data_ex.http_code,
                         content={
                             "message":f"No user found with this id > {user_id}"
                         })
        except TicketAppException as app_exc:
            return JSONResponse(status_code=app_exc.http_code,
                         content={
                             "message":f"Error during user search > {user_id}"
                         })
        except DataFileLoadException as df_exc:
            return JSONResponse(status_code=df_exc.http_code,
                         content={
                             "message":f"Error while loading data > {user_id}"
                         })
        except Exception as exc:
            return JSONResponse(status_code=500,
                         content={
                             "message":f"Unknown error > {traceback.format_exception_only(exc)}"
                         })
        return user

    @router.get("/user")
    def get_all_user(self,q: Union[str, None] = None):
        filtered_users:list[UserModel]=[]     
        
        filtered_users = user_service.getAllUser()

        return filtered_users


if __name__ == "__main__":
    myrouter = UserRouter()
    print("Hello", myrouter.get_one_user("u011").__len__())