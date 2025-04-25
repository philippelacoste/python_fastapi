from typing import Union
import uuid
import uvicorn

from fastapi import FastAPI


app = FastAPI()

from endpoints.ticket_api import router as ticket_router
from endpoints.user_api import router as user_router
from endpoints.device_api import router as device_router


@app.get("/")
def read_root(q: Union[str, None] = None):
        # renvoyer Hello World 'Synchrone' [uuid] my_uuid = uuid.uuid4()
        # ajouter un paramètre de type string à cette méthode et le renvoyer dans le json (à côté du Hello)
        my_uuid = uuid.uuid4()
        return {f"Hello {q}": f"World 'Synchrone' { my_uuid.__str__() }"}


app.include_router(ticket_router)
app.include_router(user_router)
app.include_router(device_router)

#créer le router pour les utilisateurs / users > user_api

#créer le router pour les postes informatiques / devices > device_api


if __name__ == "__main__":
    # with open("./config/config.json", "r", encoding="utf-8") as f:
    #     config = json.load(f)
    uvicorn.run("main:app")