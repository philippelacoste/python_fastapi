import json
from typing import Union

from fastapi import FastAPI

app = FastAPI()

def logged(f):
     def wrapper(*args, **kwargs):
        print(f"Début : {f.__name__}")
        value = f(*args, **kwargs)
        print(f"Fin : {f.__name__}")
        return value

@app.get("/")
def read_root():
    return {"Hello": "World"}

from datetime import datetime, date, timedelta

@logged
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    params = urllib.parse.parse_qs(q)
    data = read_data()
    date_param = params["update_date"][0]
    date_update = date_from_query_param(date_param) + timedelta(hours=3)
    data_filtered = filter(lambda x: 
                           datetime.fromisoformat(x['update_date']).timestamp() > date_update.timestamp()
                           ,
                           data)
    result = list(data_filtered)
    return result

def read_data()->list:
    with open("./data/sample_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["tickets"]

def date_from_query_param(date_q:str)->datetime:
    date_update = datetime.strptime(date_q, "%Y-%m-%d_%H:%M:%S")
    return date_update

import urllib
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app")