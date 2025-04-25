from datetime import datetime


class UserModel:
    id:str=""
    name:str=""
    email:str=""
    password:str=""
    last_login_date:datetime
    active:bool = False
    role:str=""