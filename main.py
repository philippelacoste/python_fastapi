from datetime import datetime, date, timedelta
from typing import Union
import uuid
import urllib
import uvicorn

from fastapi import APIRouter, FastAPI

from services.utils.data_services import load_data

app = FastAPI()

from endpoints.ticket_api import router


@app.get("/")
def read_root(q: Union[str, None] = None):
        # renvoyer Hello World 'Synchrone' [uuid] my_uuid = uuid.uuid4()
        # ajouter un paramètre de type string à cette méthode et le renvoyer dans le json (à côté du Hello)
        my_uuid = uuid.uuid4()
        return {f"Hello {q}": f"World 'Synchrone' { my_uuid.__str__() }"}


app.include_router(router)


if __name__ == "__main__":
    # with open("./config/config.json", "r", encoding="utf-8") as f:
    #     config = json.load(f)
    uvicorn.run("main:app")